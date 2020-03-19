#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from appium import webdriver
from utils import ios_utils
from lib import HTMLTestReport
import time

class IosEkycPerfomanceTestMan(unittest.TestCase):
    """ 정상 케이스:신분증과 동일한 인물 (男) """

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

        # ToDo systemport
        desired_caps['systemPort'] = 8212
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.daf = HTMLTestReport.DirAndFiles()

        self.driver.find_element_by_accessibility_id("record btn rotate").click()
        self.driver.find_element_by_accessibility_id("S").click()
        time.sleep(2)

    """ 정상 케이스:신분증과 동일한 인물 (男) """
    def test001_check_sameface_man_01_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_01.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_01_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test002_check_sameface_man_01_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""

        image_path = "ekyc/testData/selfie/selfie_man_01_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test003_check_sameface_man_01_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_01_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test004_check_sameface_man_02_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_02.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_02_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test005_check_sameface_man_02_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_02_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test006_check_sameface_man_02_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_02_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test007_check_sameface_man_03_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_03.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_03_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test008_check_sameface_man_03_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_03_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test009_check_sameface_man_03_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_03_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test010_check_sameface_man_04_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_04.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_04_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test011_check_sameface_man_04_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_04_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test012_check_sameface_man_04_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_04_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test013_check_sameface_man_05_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_05.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_05_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test014_check_sameface_man_05_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_05_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test015_check_sameface_man_05_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_05_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test016_check_sameface_man_06_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_06.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_06_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test017_check_sameface_man_06_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""

        image_path = "ekyc/testData/selfie/selfie_man_06_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test018_check_sameface_man_06_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_06_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test019_check_sameface_man_07_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_07.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_07_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test020_check_sameface_man_07_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_07_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test021_check_sameface_man_07_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_07_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test022_check_sameface_man_08_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""

        image_path = "ekyc/testData/license/license_man_08.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_08_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test023_check_sameface_man_08_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_08_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test024_check_sameface_man_08_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_08_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test025_check_sameface_man_09_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_09.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_09_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test026_check_sameface_man_09_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_09_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test027_check_sameface_man_09_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_09_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test028_check_sameface_man_10_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_10.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_10_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test029_check_sameface_man_10_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_10_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test030_check_sameface_man_10_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_10_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test031_check_sameface_man_11_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_11.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_11_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test032_check_sameface_man_11_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_11_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test033_check_sameface_man_11_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_11_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test034_check_sameface_man_12_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_12.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_12_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test035_check_sameface_man_12_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_12_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test036_check_sameface_man_12_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_12_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test037_check_sameface_man_13_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_13.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_13_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test038_check_sameface_man_13_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_13_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test039_check_sameface_man_13_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_13_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test040_check_sameface_man_14_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_14.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_14_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test041_check_sameface_man_14_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_14_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test042_check_sameface_man_14_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_14_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test043_check_sameface_man_15_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_15.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_15_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test044_check_sameface_man_15_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_15_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test045_check_sameface_man_15_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_15_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test046_check_sameface_man_16_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_16.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_16_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test047_check_sameface_man_16_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_16_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test048_check_sameface_man_16_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_16_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test049_check_sameface_man_17_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_17.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_17_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test050_check_sameface_man_17_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_17_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test051_check_sameface_man_17_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_17_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test052_check_sameface_man_18_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_18.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_18_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test053_check_sameface_man_18_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_18_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test054_check_sameface_man_18_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_18_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test055_check_sameface_man_19_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_19.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_19_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test056_check_sameface_man_19_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_19_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test057_check_sameface_man_19_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_19_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test058_check_sameface_man_20_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_20.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_20_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test059_check_sameface_man_20_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_20_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test060_check_sameface_man_20_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_20_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test061_check_sameface_man_21_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_21.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_21_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test062_check_sameface_man_21_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_21_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test063_check_sameface_man_21_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_21_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test064_check_sameface_man_22_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_22.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_22_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test065_check_sameface_man_22_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_22_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test066_check_sameface_man_22_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_22_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test067_check_sameface_man_23_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_23.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_23_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test068_check_sameface_man_23_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_23_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test069_check_sameface_man_23_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_23_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test070_check_sameface_man_24_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_24.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_24_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test071_check_sameface_man_24_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_24_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test072_check_sameface_man_24_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_24_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test073_check_sameface_man_25_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_25.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_25_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test074_check_sameface_man_25_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_25_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test075_check_sameface_man_25_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_25_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test076_check_sameface_man_26_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_26.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_26_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test077_check_sameface_man_26_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_26_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test078_check_sameface_man_26_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_26_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test079_check_sameface_man_27_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_27.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_27_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test080_check_sameface_man_27_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_27_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test081_check_sameface_man_27_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_27_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test082_check_sameface_man_28_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_28.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_28_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test083_check_sameface_man_28_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_28_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test084_check_sameface_man_28_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_28_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test085_check_sameface_man_29_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_29.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_29_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test086_check_sameface_man_29_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_29_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test087_check_sameface_man_29_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_29_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test088_check_sameface_man_30_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_30.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_30_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test089_check_sameface_man_30_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_30_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test090_check_sameface_man_30_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_30_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test091_check_sameface_man_31_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_31.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_31_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test092_check_sameface_man_31_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_31_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test093_check_sameface_man_31_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""

        image_path = "ekyc/testData/selfie/selfie_man_31_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test094_check_sameface_man_32_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_32.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_32_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test095_check_sameface_man_32_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_32_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test096_check_sameface_man_32_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_32_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test097_check_sameface_man_33_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_33.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_33_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test098_check_sameface_man_33_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_33_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test099_check_sameface_man_33_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_33_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test100_check_sameface_man_34_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_34.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_34_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test101_check_sameface_man_34_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_34_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test102_check_sameface_man_34_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_34_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test103_check_sameface_man_35_normal(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_man_35.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_man_35_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test104_check_sameface_man_35_bright(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_35_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test105_check_sameface_man_35_dark(self):
        """본인인증 촬영 테스트 (男): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_man_35_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
