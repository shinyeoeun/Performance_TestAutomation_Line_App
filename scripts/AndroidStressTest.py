#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import unittest
import pytest
from appium import webdriver
from utils import android_utils
from lib import HTMLTestReport
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction


class StressTestCase(unittest.TestCase):
    """ 테스트카테고리: Yuki QA Automation """

    CATEGORY_INDEX = 16  # 카테고리 인덱스
    STICKER_ID_LIST = ["63158", "63133"]
    REMOTE_URL = 'http://127.0.0.1:4723/wd/hub'

    @classmethod
    def setUpClass(self):

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8',
            'automationName': 'UiAutomator2',
            'newCommandTimeout': '180',
            'deviceName': 'Samsung Galaxy S10',
            'appPackage': 'com.linecorp.yuki',
            'appActivity': '.EffectDemoActivity',
            'udid': 'RF8M512ASVM',
            'noReset': 'true',
            'clearDeviceLogsOnStart': 'true',
            'systemPort': '8212',
        }
        self.driver = webdriver.Remote(self.REMOTE_URL, desired_caps)
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.daf = HTMLTestReport.DirAndFiles()
        self.screenX = self.driver.get_window_size().get("width")
        self.screenY = self.driver.get_window_size().get("height")
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = TouchAction(self.driver)

        # yuki-Demo 메뉴 > Camera Tap
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Camera(Integration)")').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/face_sticker_button')))

        # Target Category 탭
        self.driver.find_element_by_id("com.linecorp.yuki:id/face_sticker_button").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/sticker_category_view')))
        # android_utils.tapTargetCategory(self, int(self.CATEGORY_INDEX))
        # self.driver.find_element_by_id("com.linecorp.yuki:id/qa_play_button").click()

        # 2.이펙트 N카테고리의 63158(돈다발) 이펙트를 적용
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.STICKER_ID_LIST[0]+'")').click()
        self.driver.back()

        self.driver.find_element_by_id("com.linecorp.yuki:id/camera_mode_video").click()

    def test01_recordVideo(self):
        """ 동영상 반복촬영 """

        print("[테스트 시나리오]")
        print("1.유키데모에서 카메라메뉴실행")
        print("2.이펙트 N카테고리의 63158(돈다발) 이펙트를 적용하고 동영상촬영을 시작")
        print("3.3초정도 동영상촬영후 중지 > 다시 동영상촬영")
        print("4.해당 스텝을 반복")

        print("[LOG]=============== 테스트 시작")

        try:
            for i in range(5):
                time.sleep(5)
                # 동영상 촬영 개시
                TouchAction(self.driver).tap(None, 550, 1950, 1).perform()
                # 3초간 대기
                time.sleep(3)
                # 동영상 촬영 종료
                TouchAction(self.driver).tap(None, 550, 1950, 1).perform()

        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        finally:
            self.driver.back()

        print("[RESULT]=============== Success: 동영상 연속촬영")
        print("[LOG]=============== 테스트 종료")

    def test02_takePicture(self):
        """ 사진반복촬영 """
        print("[테스트 시나리오]")
        print("1.이펙트 N카테고리의 63158(돈다발)이펙트를 적용하고 사진촬영을 시작")
        print("2.이펙트 N카테고리의 60560 이펙트를 적용하고 사진촬영을 시작")
        print("3.이펙트 N카테고리의 63158 이펙트를 다시 적용하고 사진촬영")
        print("4.해당 스텝을 반복")

        print("[LOG]=============== 테스트 시작")
        # yuki-Demo 메뉴 > Camera Tap
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Camera(Integration)")').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/face_sticker_button')))

        # Target Category 탭
        self.driver.find_element_by_id("com.linecorp.yuki:id/face_sticker_button").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/sticker_category_view')))
        # android_utils.tapTargetCategory(self, int(self.CATEGORY_INDEX))
        # self.driver.find_element_by_id("com.linecorp.yuki:id/qa_play_button").click()

        try:
            # 1.이펙트 N카테고리의 63158(돈다발)이펙트를 적용하고 사진촬영을 시작
            TouchAction(self.driver).tap(
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.STICKER_ID_LIST[0]+'")')).perform()
            self.driver.back()
            TouchAction(self.driver).tap(
                self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation")).perform()
            TouchAction(self.driver).tap(None, 100, 1950, 1).perform()

            # 5.해당 스텝을 5회 반복
            for i in range(5):
                # 2.이펙트 N카테고리의 60560 이펙트를 적용하고 사진촬영을 시작
                TouchAction(self.driver).tap(self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.STICKER_ID_LIST[1]+'")')).perform()
                self.driver.back()
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation")).perform()
                time.sleep(4)
                TouchAction(self.driver).tap(None, 100, 1950, 1).perform()

                # 3.이펙트 N카테고리의 63158 이펙트를 다시 적용하고 사진촬영
                TouchAction(self.driver).tap(self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+self.STICKER_ID_LIST[0]+'")')).perform()
                self.driver.back()
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation")).perform()
                time.sleep(4)
                TouchAction(self.driver).tap(None, 100, 1950, 1).perform()
                time.sleep(3)

        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)

        print("[RESULT]=============== Success: 사진 연속촬영")
        print("[LOG]=============== 테스트 종료")

    def test03_ratioChange(self):
        """ 화면비율변경 """
        print("[테스트 시나리오]")
        print("1.이펙트 N카테고리의 63158(돈다발)이펙트를 적용하고 비율버튼을 탭")
        print("2.9:16>3:4>1:1비율을 순서대로 적용")
        print("3.해당 스텝을 20회 반복")

        print("[LOG]=============== 테스트 시작")

        try:
            for i in range(4):
                for roop in range(3):
                    TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/ratio_button")).perform()

        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)

        print("[RESULT]=============== Success: 화면비율변경")
        print("[LOG]=============== 테스트 종료")

    def test04_cameraSwitch(self):
        """ 카메라방향전환 """
        print("[테스트 시나리오]")
        print("1.이펙트 N카테고리의 63158(돈다발)이펙트를 적용하고 비율버튼을 탭")
        print("2.out 카메라 > in 카메라 순서대로 적용")
        print("3.해당 스텝을 20회 반복")

        print("[LOG]=============== 테스트 시작")
        try:
            for i in range(4):
                for roop in range(2):
                    TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/turn_button")).perform()
                    time.sleep(2)

        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)

        print("[RESULT]=============== Success: 카메라방향전환")
        print("[LOG]=============== 테스트 종료")

    def test05_deviceLockUnlock(self):
        """ 디바이스 Lock/Unlock """
        print("[테스트 시나리오]")
        print("1.이펙트 N카테고리의 63158(돈다발)이펙트를 적용")
        print("2.이펙트 N카테고리의 63158(돈다발)이펙트를 다시 탭하여 적용해제 ")
        print("3.해당 스텝을 20회 반복")

        print("[LOG]=============== 테스트 시작")

        try:
            for i in range(4):
                self.driver.lock(1)
                self.driver.unlock()
                time.sleep(1)

        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)

        print("[RESULT]=============== Success: 디바이스 Lock/Unlock")
        print("[LOG]=============== 테스트 종료")


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        os.popen("adb shell rm -r sdcard/DCIM/LINE")


if __name__ == '__main__':
    unittest.main()
    unittest.main(warnings='ignore')
