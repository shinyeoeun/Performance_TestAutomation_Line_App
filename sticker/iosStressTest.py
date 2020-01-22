#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import unittest
from appium import webdriver
from lib import HTMLTestReport
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction


class StressTest(unittest.TestCase):
    """ 테스트카테고리: Yuki QA Automation """

    CATEGORY_INDEX = 4  # 카테고리 인덱스
    SWIPE_DURATION_DEFAULT = 1500  # Swipe 기본값

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
        self.stickerX = 40
        self.stickerY = 630

        # 마스터영상 표시
        self.driver.find_element_by_id("pip icon play normal").click()
        time.sleep(3)
        # sticker list 버튼 탭
        self.driver.find_element_by_accessibility_id("camera sticker").click()
        time.sleep(2)
        # 카테고리 보일때까지 스와이프
        self.driver.swipe(350, 755, 70, 755, self.SWIPE_DURATION_DEFAULT)
        # 카테고리 탭
        TouchAction(self.driver).tap(None, 160, 760, 1).perform()
        time.sleep(1)
        # 스티커적용
        TouchAction(self.driver).tap(None, self.stickerX+70, self.stickerY, 1).perform()
        # 스티커리스트 숨김
        TouchAction(self.driver).tap(None, self.screenX/2, self.screenY/2, 1).perform()

    def test01_recordVideo(self):
        """ 동영상 반복촬영 """
        print("[테스트 시나리오]")
        print("1.유키데모에서 카메라메뉴실행")
        print("2.이펙트 N카테고리의 63158(돈다발) 이펙트를 적용하고 동영상촬영을 시작")
        print("3.3초정도 동영상촬영후 중지 > 다시 동영상촬영")
        print("4.해당 스텝을 반복")

        try:
            for i in range(3):
                # 녹화시작
                TouchAction(self.driver).press(self.driver.find_element_by_id("filter select fixed 1")).wait(501).release().perform()
                time.sleep(3)
                # 녹화정지
                self.driver.find_element_by_id("recorder btn stop").click()
                time.sleep(1)
                # 다이얼로그 탭
                self.driver.find_element_by_id("OK").click()
                time.sleep(1)

        except Exception:
            self.assertTrue(False)

        print("[RESULT]=============== Success: 사진 연속촬영")
        print("[LOG]=============== 테스트 종료")


    def test02_takePicture(self):
        """ 사진반복촬영 """
        print("[테스트 시나리오]")
        print("1.이펙트 N카테고리의 63158(돈다발)이펙트를 적용하고 사진촬영을 시작")
        print("2.이펙트 N카테고리의 60560 이펙트를 적용하고 사진촬영을 시작")
        print("3.이펙트 N카테고리의 63158 이펙트를 다시 적용하고 사진촬영")
        print("4.해당 스텝을 반복")

        try:
            for i in range(3):
                # 사진촬영
                self.driver.find_element_by_id("filter select fixed 1").click()
                time.sleep(1)
                # 다운로드아이콘 표시
                TouchAction(self.driver).tap(None, self.screenX/2, self.screenY/2, 1).perform()
                time.sleep(1)
                # 다운로드 아이콘 탭
                self.driver.find_element_by_id("sticker debug down").click()

                # 다이얼로그 2개 탭
                for i in range(2):
                    self.driver.find_element_by_id("OK").click()
                    time.sleep(1)

                self.driver.find_element_by_id("camera icon close 01").click()
                time.sleep(1)

                # 스티커 전환: 60560
                self.driver.find_element_by_accessibility_id("camera sticker").click()
                TouchAction(self.driver).tap(None, self.stickerX+140, self.stickerY, 1).perform()
                TouchAction(self.driver).tap(None, self.screenX/2, self.screenY/2, 1).perform()

                # 사진촬영
                self.driver.find_element_by_id("filter select fixed 1").click()
                time.sleep(1)
                TouchAction(self.driver).tap(None, self.screenX/2, self.screenY/2, 1).perform()
                time.sleep(1)
                self.driver.find_element_by_id("sticker debug down").click()

                for i in range(2):
                    self.driver.find_element_by_id("OK").click()
                    time.sleep(1)

                self.driver.find_element_by_id("camera icon close 01").click()
                time.sleep(1)

                # 스티커 전환: 60560
                self.driver.find_element_by_accessibility_id("camera sticker").click()
                TouchAction(self.driver).tap(None, self.stickerX+70, self.stickerY, 1).perform()
                TouchAction(self.driver).tap(None, self.screenX/2, self.screenY/2, 1).perform()

        except Exception:
            self.assertTrue(False)

        print("[RESULT]=============== Success: 사진 연속촬영")
        print("[LOG]=============== 테스트 종료")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
