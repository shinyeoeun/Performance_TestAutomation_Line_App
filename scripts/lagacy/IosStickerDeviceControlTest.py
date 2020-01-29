#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from lib import HTMLTestReport
import pandas as pd


class IosStickerDeviceControlTest(unittest.TestCase):
    """ Yuki Demo: dev Y-3 카테고리 스티커 적용테스트"""

    SWIPE_DURATION_DEFAULT = 1500  # Swipe 기본값
    # ToDo 카테고리 인덱스 지정
    CATEGORY_INDEX = 9
    stickerX = 40
    stickerY = 630
    STICKER_ID_LIST = {}
    TEST_ENV_INFO = {}

    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '12.1'
        desired_caps['deviceName'] = 'LFK-5776'
        desired_caps['udid'] = '00008020-000C256A0281002E'
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['bundleId'] = 'com.linecorp.yuki'
        desired_caps['noReset'] = 'true'
        desired_caps['usePrebuiltWDA'] = 'true'
        desired_caps['systemPort'] = 8212
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.daf = HTMLTestReport.DirAndFiles()
        self.screenX = self.driver.get_window_size().get("width")
        self.screenY = self.driver.get_window_size().get("height")

        # 마스터영상 표시
        self.driver.find_element_by_id("pip icon play normal").click()
        time.sleep(3)

        # sticker list 버튼 탭
        self.driver.find_element_by_accessibility_id("camera sticker").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[7]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell["+str(self.CATEGORY_INDEX)+"]").click()
        time.sleep(1)

        # 스킨스무스 조절바 숨기기
        self.driver.find_element_by_id("skin smooth btn true").click()


    def test01_crash_check_on_sticker_adaption_crash_check(self):
        """Sticker: Sticker를 순차적으로 적용하였을 경우의 동작확인/ Category: dev Y-3"""
        print("[LOG] Test Start")

        for i in range(3):
            for i in range(2):
                TouchAction(self.driver).tap(None, self.stickerX, self.stickerY, 1).perform()

            sticker_id = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]").get_attribute("name")
            self.STICKER_ID_LIST['1'] = sticker_id
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            print("[LOG] Sticker Adapt Success: " + self.STICKER_ID_LIST['1'])
            self.stickerX = self.stickerX + 70

            for i in range(2):
                TouchAction(self.driver).tap(None, self.stickerX+70, self.stickerY, 1).perform()

            sticker_id = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[7]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]").get_attribute("name")
            self.STICKER_ID_LIST['2'] = sticker_id
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            print("[LOG] Sticker Adapt Success: "+ self.STICKER_ID_LIST['2'])
            self.stickerX = self.stickerX + 70

            for i in range(2):
                TouchAction(self.driver).tap(None, self.stickerX+140, self.stickerY, 1).perform()

            sticker_id = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]").get_attribute("name")
            self.STICKER_ID_LIST['3'] = sticker_id
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            print("[LOG] Sticker Adapt Success: "+ self.STICKER_ID_LIST['3'])
            self.stickerX = self.stickerX + 70

            for i in range(2):
                TouchAction(self.driver).tap(None, self.stickerX+210, self.stickerY, 1).perform()

            sticker_id = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]").get_attribute("name")
            self.STICKER_ID_LIST['4'] = sticker_id
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            print("[LOG] Sticker Adapt Success: "+ self.STICKER_ID_LIST['4'])
            self.stickerX = self.stickerX + 70

            for i in range(2):
                TouchAction(self.driver).tap(None, self.stickerX+280, self.stickerY, 1).perform()

            sticker_id = self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeScrollView/XCUIElementTypeOther[2]/XCUIElementTypeStaticText[2]").get_attribute("name")
            self.STICKER_ID_LIST['5'] = sticker_id
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            print("[LOG] Sticker Adapt Success: " + self.STICKER_ID_LIST['5'])






        print("[LOG] Success: 카테고리 내 Sticker 순차 적용 ")

    def test02_crash_check_on_sticker_change_orderly_fast(self):
        """Sticker: Sticker를 빠르게(0.1초간격으로) 전환하였을 경우의 동작확인/ Category: dev Y-3"""

        print("[LOG] Test Start")

        for i in range(1, 6):
            TouchAction(self.driver).tap(None, self.stickerX, self.stickerY, 1).perform()
            time.sleep(0.1)
            print("[LOG] Success: [" + self.STICKER_ID_LIST[str(i)]+"]")
            self.stickerX = self.stickerX + 70

        self.stickerX = 40
        print("[LOG] Success: 카테고리 내 Sticker 고속전환")

    def test03_crash_check_on_filter_change_with_sticker(self):
        """Filter: Sticker가 적용된 상태에서 Swipe로 필터변경동작확인 (Swipe 횟수: 5회)"""
        print("[LOG] Test Start")

        # 스티커 변경
        for orderly_index in range(1, 6):
            TouchAction(self.driver).tap(None, self.stickerX, self.stickerY, 1).perform()
            time.sleep(0.1)
            # 스와이프로 필터변경
            for i in range(5):
                self.driver.swipe(self.screenX*0.5, self.screenY*0.5, self.screenX, self.screenY*0.5, self.SWIPE_DURATION_DEFAULT)
                time.sleep(0.1)
            print("[LOG] Success: [" + self.STICKER_ID_LIST[str(i)]+"]")
            self.stickerX = self.stickerX + 70

        self.stickerX = 40
        print("[LOG] Success: Sticker가 적용된 상태에서 Swipe로 필터변경")

    def test04_crash_check_on_device_lock_unlock(self):
        """Device Control: Sticker 적용상태에서 Device sleep모드 on/off 전환"""
        print("[LOG] Test start")

        for i in range(1, 6):
            TouchAction(self.driver).tap(None, self.stickerX, self.stickerY, 1).perform()
            time.sleep(1)
            self.driver.lock(1)
            self.driver.unlock()
            print("[LOG] Success: [" + self.STICKER_ID_LIST[str(i)]+"]")
            self.stickerX = self.stickerX + 70

        self.stickerX = 40
        print("[LOG] Success: Sticker 적용상태에서 Device sleep모드 on/off ")

    def test05_crash_check_on_bg_fg_change_with_sticker(self):
        """Device Control: Sticker 적용상태에서 App BG/FG 전환"""
        print("[LOG] Test start")

        for i in range(1, 6):
            TouchAction(self.driver).tap(None, self.stickerX, self.stickerY, 1).perform()
            time.sleep(1)
            self.driver.background_app(1)
            print("[LOG] Success: [" + self.STICKER_ID_LIST[str(i)]+"]")
            self.stickerX = self.stickerX + 70

        self.stickerX = 40
        print("[LOG] Success:All Sticker Pass: Sticker 적용상태에서 App BG/FG")

    def test06_crash_check_on_take_photo(self):
        """Device Control: Sticker 적용상태에서 사진 촬영 (Preview mode)"""
        print("[LOG] Test start")

        for i in range(1, 6):
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            TouchAction(self.driver).tap(None, 200, 700, 1).perform()
            time.sleep(2)
            TouchAction(self.driver).tap(None, self.screenX * 0.5, self.screenY * 0.5, 1).perform()
            time.sleep(2)
            self.driver.find_element_by_id("camera icon close 01").click()
            print("[LOG] Success: [" + self.STICKER_ID_LIST[str(i)]+"]")
            self.stickerX = self.stickerX + 70
            self.driver.find_element_by_accessibility_id("camera sticker").click()

        self.stickerX = 40
        print("[LOG] Success: 사진촬영 성공")

    def test07_crash_check_on_press_volumekey(self):
        """Device Control: Sound Sticker적용 상태에서 Device volume Up/volume Down"""
        print("[LOG] Test start")

        for i in range(1, 6):
            TouchAction(self.driver).tap(None, self.stickerX, self.stickerY, 1).perform()
            self.driver.execute_script("mobile: pressButton", {'name': 'volumeup'})
            self.driver.execute_script("mobile: pressButton", {'name': 'volumedown'})
            print("[LOG] Success: [" + self.STICKER_ID_LIST[str(i)]+"]")
            self.stickerX = self.stickerX + 70

        self.stickerX = 40
        print("[LOG] Success: Sound Sticker 적용상태에서 Device volume Up/volume Down ")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
