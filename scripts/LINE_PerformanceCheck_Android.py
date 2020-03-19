#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
from appium import webdriver
from threading import Thread

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from pylab import *

MEMORY_PSS_TOTAL_VALUE_LIST = []
CPU_VALUE_LIST = []
TIME_SEC = []
SWIPE_DURATION_DEFAULT = 2700  # Swipe 기본값
TIME_OUT = 10
PACKAGE = "jp.naver.line.android"
BUILD_VERSION = "10.2.0_BETA"

@pytest.mark.parametrize("udid, system_port, device_name", [
    ("R58M46AFQGD", "8212", "Samsung Galaxy S10"), ])

def test_main(udid, system_port, device_name):
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '9',
        'udid': udid,
        'deviceName': device_name,
        'appPackage': PACKAGE,
        'appActivity': '.activity.SplashActivity',
        'automationName': 'UiAutomator2',
        'systemPort': system_port,
        'noReset': True,
        'newCommandTimeout': '180',
        'clearDeviceLogsOnStart': True,
    }

    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    wait = WebDriverWait(driver, 20)
    actions = TouchAction(driver)

    screenX = driver.get_window_size().get("width")
    screenY = driver.get_window_size().get("height")

    # 메모리측정 Thread 개시
    thread_memory = Thread(target=getPerformanceValue_memory, args=(driver, 35))
    thread_memory.start()

    wait.until(EC.element_to_be_clickable((By.ID, 'jp.naver.line.android:id/profile_view')))
    driver.find_element_by_id("jp.naver.line.android:id/profile_view").click()

    driver.find_element_by_android_uiautomator('new UiSelector().text("프로필 편집")').click()
    wait.until(EC.element_to_be_clickable((By.ID, 'jp.naver.line.android:id/settings_profile_photo_btn')))
    driver.find_element_by_id("jp.naver.line.android:id/settings_profile_photo_btn").click()

    driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.Button').click()
    time.sleep(2)
    driver.find_element_by_accessibility_id("이펙트").click()

    for i in range(3):
        sticker_parent = driver.find_element_by_id("jp.naver.line.android:id/face_sticker_item_list")
        sticker_children = sticker_parent.find_elements_by_class_name("android.view.ViewGroup")
        sticker_children[0].click()

    actions.tap(None, screenX*0.5, screenY*0.5, 1).perform()
    time.sleep(20)
    driver.back()
    time.sleep(5)

    # 메모리측정 Thread 종료
    thread_memory.join()

    driver.quit()
    generateGraph_memory()
    getRawDataMemory()

# 메모리 취득 쓰레드
def getPerformanceValue_memory(driver, sec):
    for i in range(sec):
        TIME_SEC.append(time.strftime("%H:%M:%S"))
        MEMORY_LIST = driver.get_performance_data(PACKAGE, "memoryinfo", TIME_OUT)
        MEMORY_PSS_TOTAL_VALUE = MEMORY_LIST[1]
        MEMORY_PSS_TOTAL_VALUE_LIST.append(int(MEMORY_PSS_TOTAL_VALUE[5]))
        time.sleep(1)

# 로우데이터 CSV작성
def getRawDataMemory():
    raw_data = pd.DataFrame({'Time': TIME_SEC,'RAM Usage(Total PSS(KB))': MEMORY_PSS_TOTAL_VALUE_LIST}, columns=['Time', 'Total PSS(KB)'])
    raw_data.to_csv("LINE_ChatRoom_memory_raw_data_" + BUILD_VERSION + ".csv", index=False)

# 메모리 그래프 작성
def generateGraph_memory():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(TIME_SEC, MEMORY_PSS_TOTAL_VALUE_LIST)
    ax.set_title('LINE Chat Room Memory Check(Build Ver:' + BUILD_VERSION + ')')
    ax.set_ylabel('Total PSS(KB)')
    ax.set_xlabel('TIME(sec)')
    ax.grid(True)
    plt.xticks(TIME_SEC, rotation='vertical')
    plt.show()
