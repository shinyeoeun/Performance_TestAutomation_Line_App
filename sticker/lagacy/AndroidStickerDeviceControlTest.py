#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import unittest
from appium import webdriver
from utils import android_utils
from lib import HTMLTestReport
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction

class AndroidStickerDeviceControlTest(unittest.TestCase):
    """ 테스트카테고리: Yuki QA Automation """

    SWIPE_DURATION_DEFAULT = 2700  # Swipe시간 기본값
    CATEGORY_INDEX = 8  # 카테고리 인덱스
    STICKER_NOTICE_OPEN_MOUSE = "Open your mouth"
    STICKER_LIST = ["61609", "62141", "61958", "62638", "60847", "60763", "60143", "60844", "61771", "61800"]

    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['newCommandTimeout'] = '180'
        desired_caps['deviceName'] = 'Samsung Galaxy S10'
        desired_caps['appPackage'] = 'com.linecorp.yuki'
        desired_caps['appActivity'] = '.EffectDemoActivity'
        desired_caps['udid'] = 'RF8M512ASVM'
        desired_caps['noReset'] = 'true'
        desired_caps['clearDeviceLogsOnStart'] = 'true'
        desired_caps['systemPort'] = 8212
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.daf = HTMLTestReport.DirAndFiles()
        self.screenX = self.driver.get_window_size().get("width")
        self.screenY = self.driver.get_window_size().get("height")
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = TouchAction(self.driver)
        BUILD_INFO = self.driver.find_element_by_id("com.linecorp.yuki:id/text_info_2").get_attribute("text").split("ver:")[1].split(",")[0]
        print(BUILD_INFO)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/text_info_1')))

        # yuki-Demo 메뉴 > Camera Tap
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Camera(Integration)")').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/face_sticker_button')))

        # Target Category 탭
        self.driver.find_element_by_id("com.linecorp.yuki:id/face_sticker_button").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/sticker_category_view')))
        self.driver.swipe(self.screenX * 0.9, self.screenY * 0.98, self.screenX * 0.1, self.screenY * 0.98, self.SWIPE_DURATION_DEFAULT)
        time.sleep(3)
        android_utils.tapTargetCategory(self, int(self.CATEGORY_INDEX))

    # ==========================

    def test001_flash_activation_01(self):
        """ Flash 버튼 동작 확인 """
        print("[LOG]=============== TEST START " + self.STICKER_LIST[0])
        TouchAction(self.driver).tap(self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + self.STICKER_LIST[0] + '")')).perform()
        self.driver.back()

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/turn_button").click()
            time.sleep(1)
            self.driver.find_element_by_id("com.linecorp.yuki:id/flash_button").click()
            print("[LOG]=============== 플래쉬 OFF")
            self.driver.find_element_by_id("com.linecorp.yuki:id/flash_button").click()
            print("[LOG]=============== 플래쉬 AUTO")
            self.driver.find_element_by_id("com.linecorp.yuki:id/flash_button").click()
            print("[LOG]=============== 플래쉬 ON")
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            assert False, "Flash 버튼 동작 fail"
        else:
            assert True, "Flash 버튼 동작 성공"
        print("[RESULT]=============== Success: Flash 버튼 동작 확인")

    def test002_camera_rotate_01(self):
        """ 스티커 적용상태에서 카메라 In/out 변경 """

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/turn_button").click()
            time.sleep(2)
            print("[LOG]=============== 헤더 버튼 탭으로 카메라 방향전환: OUT")
            self.driver.find_element_by_id("com.linecorp.yuki:id/turn_button").click()
            time.sleep(2)
            print("[LOG]=============== 헤더 버튼 탭으로 카메라 방향전환: IN")
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 카메라 In/out 변경")

    def test003_ratio_switch_01(self):
        """ 스티커 적용상태에서 화면비율변경 """
        self.driver.find_element_by_id("com.linecorp.yuki:id/qa_play_button").click()
        time.sleep(2)

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/ratio_button").click()
            self.daf.get_screenshot(self.driver)
            print("[LOG]=============== 화면비율: 3:4")
            self.driver.find_element_by_id("com.linecorp.yuki:id/ratio_button").click()
            self.daf.get_screenshot(self.driver)
            print("[LOG]=============== 화면비율: 1:1")
            self.driver.find_element_by_id("com.linecorp.yuki:id/ratio_button").click()
            self.daf.get_screenshot(self.driver)
            print("[LOG]=============== 화면비율: 9:16")
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[LOG]=============== Success: 스티커 적용상태에서 화면비율변경")

    def test004_blur_bar_01(self):
        """ 스티커 적용상태에서 Blur bar 조절 """

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/blur_button").click()
            self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/blur_value')))
            self.driver.find_element_by_id("com.linecorp.yuki:id/blur_seekbar").send_keys(100)
            self.daf.get_screenshot(self.driver)
            self.driver.find_element_by_id("com.linecorp.yuki:id/blur_seekbar").send_keys(0)
            self.driver.find_element_by_id("com.linecorp.yuki:id/blur_button").click()
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 Blur bar 조절")

    def test005_skin_smooth_01(self):
        """ 스티커 적용상태에서 Skin smooth 조절 """

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/skin_smooth_button").click()
            self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/skin_smooth_value')))
            self.driver.find_element_by_id("com.linecorp.yuki:id/skin_smooth_seekbar").send_keys(200)
            self.daf.get_screenshot(self.driver)
            self.driver.find_element_by_id("com.linecorp.yuki:id/skin_smooth_seekbar").send_keys(0)
            self.driver.find_element_by_id("com.linecorp.yuki:id/skin_smooth_button").click()
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 Skin smooth 조절")

    def test006_swipe_action_01(self):
        """ 스티커 적용상태에서 스와이프로 필터전환 """

        try:
            for i in range(3):
                self.driver.swipe(self.screenX * 0.5, self.screenY * 0.5, self.screenX * 0.1, self.screenY * 0.5, self.SWIPE_DURATION_DEFAULT)
            print("[LOG]=============== 스와이프로 필터전환")
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 스와이프로 필터전환")

    def test007_filter_List_01(self):
        """ 스티커 적용상태에서 사진촬영 """

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/filter_button").click()
            self.assertTrue(self.driver.find_element_by_id("com.linecorp.yuki:id/screen_filter_list").is_displayed(), "필터리스트 표시 실패")
            self.assertTrue(self.driver.find_element_by_id("com.linecorp.yuki:id/filter_category_view").is_displayed(), "필터카테고리리스트 표시 실패")
            self.driver.back()
            self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/camera_mode_image')))
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 사진/비디오 촬영")

    def test008_take_photo_01(self):
        """ 스티커 적용상태에서 사진촬영 """

        try:
            self.driver.find_element_by_id("com.linecorp.yuki:id/camera_mode_image").click()
            print("[LOG]=============== 카메라 모드: 이미지")
            self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation").click()
            print("[LOG]=============== 사진 촬영")
            self.driver.find_element_by_id("com.linecorp.yuki:id/camera_mode_video").click()
            print("[LOG]=============== 카메라 모드: 비디오")
            self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation").click()
            print("[LOG]=============== 비디오 녹화 시작")
            self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/recording_time')))
            self.driver.find_element_by_id("com.linecorp.yuki:id/resume_pause_button").click()
            print("[LOG]=============== 비디오 녹화 일시정지")
            self.driver.find_element_by_id("com.linecorp.yuki:id/resume_pause_button").click()
            print("[LOG]=============== 비디오 녹화 재개")
            self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation").click()
            print("[LOG]=============== 비디오 녹화 종료")
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 사진/비디오 촬영")

    def test009_app_bg_fg_01(self):
        """ 스티커 적용상태에서 App BG/FG """

        try:
            self.driver.background_app(2)
            self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/text_info_1')))
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("Camera(Integration)")').click()
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스티커 적용상태에서 App BG/FG")
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/face_sticker_button')))
        self.driver.find_element_by_id("com.linecorp.yuki:id/face_sticker_button").click()
        time.sleep(1)
        self.driver.swipe(self.screenX * 0.9, self.screenY * 0.98, self.screenX * 0.1, self.screenY * 0.98, self.SWIPE_DURATION_DEFAULT)
        time.sleep(2)
        android_utils.tapTargetCategory(self, int(self.CATEGORY_INDEX))
        self.driver.find_element_by_id("com.linecorp.yuki:id/qa_play_button").click()

    def test010_stress_test_01(self):
        """ 스트레스 테스트 """
        print("[LOG]=============== TEST START " + self.STICKER_LIST[0])

        try:
            # 적용된 스티커 연속탭
            for i in range(5):
                TouchAction(self.driver).tap(self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + self.STICKER_LIST[0] + '")')).perform()
            time.sleep(1)
            # 비율버튼 연속 탭
            for i in range(6):
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/ratio_button")).perform()
            time.sleep(1)
            # 카메라방향전환버튼 연속 탭
            for i in range(4):
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/turn_button")).perform()
            time.sleep(1)
            # 블러버튼 연속 탭
            for i in range(4):
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/blur_button")).perform()
            time.sleep(1)
            # 스킨스무스버튼 연속 탭
            for i in range(4):
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/skin_smooth_button")).perform()
            time.sleep(1)
            # 화면중앙 연속 탭
            for i in range(4):
                TouchAction(self.driver).tap(None, self.screenX*0.5, self.screenY*0.5).perform()
            time.sleep(1)
            # 사진촬영버튼 연속 탭
            for i in range(4):
                TouchAction(self.driver).tap(self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation")).perform()
        except Exception:
            self.daf.get_logcat(self.driver)
            android_utils.capture_logcat(self)
            self.assertTrue(False)
        print("[RESULT]=============== Success: 스트레스 테스트")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        os.popen("adb shell rm -r sdcard/DCIM/LINE")

if __name__ == '__main__':
    unittest.main()
