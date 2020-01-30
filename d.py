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
import os

SWIPE_DURATION_DEFAULT = 3000
TIME_SEC = []
TIME_OUT = [1]
PACKAGE = "com.linecorp.yuki"
# STICKER_ID_LIST = ["61609", "62141", "61958", "62638", "60847", "60763", "60143", "60844", "61771", "61800"]
STICKER_ID_LIST = ["61609", "62141"]
RAW_DATA = []
CPU = []
CATEGORY_INDEX = 18
CPU_VALUE_LIST = []

@pytest.mark.parametrize("udid, system_port, device_name", [
    ("RF8M512ASVM", "8000", "Samsung Galaxy S10"), ]
                         )
def test_main(udid, system_port, device_name):
    print("[LOG]=============== TEST START ===============")
    capabilities = {
        'platformName': 'Android',
        'automationName': 'UiAutomator2',
        'deviceName': device_name,
        'appPackage': PACKAGE,
        'appActivity': '.EffectDemoActivity',
        'udid': udid,
        'systemPort': system_port,
        'noReset': True,
        'newCommandTimeout': '180',
    }

    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    screenX = driver.get_window_size().get("width")
    screenY = driver.get_window_size().get("height")
    wait = WebDriverWait(driver, 20)
    actions = TouchAction(driver)

    # yuki-Demo 메뉴 > Camera Tap
    driver.find_element_by_android_uiautomator('new UiSelector().text("Camera(Integration)")').click()
    wait.until(EC.element_to_be_clickable((By.ID, PACKAGE + ':id/face_sticker_button')))

    # Target Category 탭
    driver.find_element_by_id(PACKAGE + ":id/face_sticker_button").click()
    wait.until(EC.element_to_be_clickable((By.ID, PACKAGE + ':id/sticker_category_view')))

    driver.swipe(screenX * 0.9, screenY * 0.98, screenX * 0.1, screenY * 0.98, SWIPE_DURATION_DEFAULT)
    time.sleep(3)
    tapTargetCategory(driver, int(CATEGORY_INDEX))

    # 메모리측정 Thread 개시
    t2 = Thread(target=getPerformanceValue_cpu, args=(driver, 30))
    t2.start()

    for i in range(len(STICKER_ID_LIST)):

        if STICKER_ID_LIST[i] is "60763":
            driver.swipe(screenX / 2, screenY * 0.9, screenX / 2, screenY * 0.8, SWIPE_DURATION_DEFAULT)

        driver.find_element_by_android_uiautomator('new UiSelector().text("' + STICKER_ID_LIST[i] + '")').click()

        # 화면비율변경
        for roop in range(3):
            driver.find_element_by_id(PACKAGE + ":id/ratio_button").click()

        # 카메라방향전환
        for roop in range(2):
            driver.find_element_by_id(PACKAGE + ":id/turn_button").click()
            time.sleep(2)

    # 메모리측정 Thread 종료
    t2.join()

    driver.quit()
    getRawDataCpu(TIME_SEC, CPU_VALUE_LIST)


def tapTargetCategory(driver, index):
    sticker_parent = driver.find_element_by_id("com.linecorp.yuki:id/sticker_category_view")
    sticker_children = sticker_parent.find_elements_by_class_name("android.widget.FrameLayout")
    sticker_children[index].find_element_by_class_name("android.widget.FrameLayout").click()


def tapTargetSticker(driver, sticker_id):
    driver.find_element_by_android_uiautomator('new UiSelector().text("' + sticker_id + '")').click()
    driver.back()


def getPerformanceValue_cpu(driver, roopcount):
    print("[LOG]=============== resource measurement start ===============")
    for index in range(roopcount):
        TIME_SEC.append(time.strftime("%H:%M:%S"))
        CPU_LIST = os.popen("adb shell top -n 1 | findstr com.linecorp.yu+").readline().split()[8]
        CPU_VALUE_LIST.append(CPU_LIST[0:2])
        print("[LOG] CPU data: " + CPU_LIST[0:2])
    print("[LOG]=============== resource measurement end ===============")

def getRawDataCpu(TIME_SEC, CPU_VALUE_LIST):
    RAW_DATA = pd.DataFrame({'Time': TIME_SEC, 'cpu': CPU_VALUE_LIST}, columns=['Time', 'cpu'])
    RAW_DATA.to_csv("yuki_cpu_raw_data.csv", index=False)

def getCurrentTime():
    currentTime = time.strftime("%H:%M:%S")
    return currentTime


def generateGraph_cpu():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks([0, 15, 30])
    # ax.set_xticks(np.arange(len(MEMORY_PSS_TOTAL_VALUE_LIST)))
    ax.set_xticklabels(STICKER_ID_LIST, rotation=45)
    ax.set_title('Yuki SDK CPU Usage')
    ax.set_ylabel('CPU(%)')
    ax.set_xlabel('Sticker ID')
    ax.plot(CPU)
    plt.show()
