#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pytest
from appium import webdriver
import time
import matplotlib.pyplot as plt
from threading import Thread
import numpy as np
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from pylab import *

SWIPE_DURATION_DEFAULT = 2800
MEMORY = []
MEMORY_PSS_TOTAL_VALUE = []
MEMORY_PSS_TOTAL_VALUE_LIST = []
TIME_SEC = []
TIME_OUT = [1]
PACKAGE = "com.linecorp.yuki"
STICKER_ID_LIST = ["61609", "62141", "61958", "62638", "60847", "60763", "60143", "60844", "61771", "61800"]
#STICKER_ID_LIST = ["61609", "62141"]
RAW_DATA = []

CATEGORY_INDEX = 18

@pytest.mark.parametrize("udid, system_port, device_name", [
    ("RF8M512ASVM", "8000", "Samsung Galaxy S10"),]
                         )

def test_main (udid, system_port, device_name):
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
    t1 = Thread(target=getPerformanceValue_thread, args=(driver, 300))
    t1.start()

    for i in range(len(STICKER_ID_LIST)):

        if STICKER_ID_LIST[i] is "60763":
            driver.swipe(screenX/2, screenY * 0.9, screenX/2, screenY * 0.8, SWIPE_DURATION_DEFAULT)

        driver.find_element_by_android_uiautomator('new UiSelector().text("'+STICKER_ID_LIST[i]+'")').click()

        # 화면비율변경
        for roop in range(3):
            driver.find_element_by_id(PACKAGE + ":id/ratio_button").click()

        # 카메라방향전환
        for roop in range(2):
            driver.find_element_by_id(PACKAGE + ":id/turn_button").click()
            time.sleep(2)

        # 디바이스 Lock/Unlock
        driver.lock(1)
        driver.unlock()

    # 메모리측정 Thread 종료
    t1.join()

    driver.quit()
    getRawData(TIME_SEC, MEMORY_PSS_TOTAL_VALUE_LIST)
    generateGraph()

def tapTargetCategory(driver, index):
    sticker_parent = driver.find_element_by_id("com.linecorp.yuki:id/sticker_category_view")
    sticker_children = sticker_parent.find_elements_by_class_name("android.widget.FrameLayout")
    sticker_children[index].find_element_by_class_name("android.widget.FrameLayout").click()

def tapTargetSticker(driver, sticker_id):
    driver.find_element_by_android_uiautomator('new UiSelector().text("'+sticker_id+'")').click()
    driver.back()

def getPerformanceValue_thread(driver, roopCount):
    print("[LOG]=============== resource measurement start ===============")
    for index in range(roopCount):
        TIME_SEC.append(time.strftime("%H:%M:%S"))
        MEMORY_LIST = driver.get_performance_data(PACKAGE, "memoryinfo", TIME_OUT)
        MEMORY_PSS_TOTAL_VALUE = MEMORY_LIST[1]
        MEMORY_PSS_TOTAL_VALUE_LIST.append(int(MEMORY_PSS_TOTAL_VALUE[5]))
        print("[LOG] Memory data: " + MEMORY_PSS_TOTAL_VALUE[5])
    print("[LOG]=============== resource measurement end ===============")


def getRawData(TIME_SEC, MEMORY_PSS_TOTAL_VALUE_LIST):
    RAW_DATA = pd.DataFrame({'Time': TIME_SEC, 'RAM Usage(Total PSS(KB))': MEMORY_PSS_TOTAL_VALUE_LIST}, columns=['Time', 'RAM Usage(Total PSS(KB))'])
    RAW_DATA.to_csv("YukiSdkMemoryRawData.csv", index=False)
    return RAW_DATA

def getCurrentTime():
    currentTime = time.strftime("%H:%M:%S")
    return currentTime

def generateGraph():

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks([0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300])
    #ax.set_xticks(np.arange(len(MEMORY_PSS_TOTAL_VALUE_LIST)))
    ax.set_xticklabels(STICKER_ID_LIST, rotation=45)
    ax.set_title('Yuki SDK Memory Usag:Total PSS(KB)')
    ax.set_ylabel('Total PSS(KB)')
    ax.set_xlabel('Sticker ID')
    ax.plot(MEMORY_PSS_TOTAL_VALUE_LIST)
    plt.show()