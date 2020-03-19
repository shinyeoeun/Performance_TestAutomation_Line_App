#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from appium import webdriver
from lib import HTMLTestReport
from utils import ios_utils
import time

class IosEkycPerfomanceTestWoman(unittest.TestCase):
    """  정상 케이스:신분증과 동일한 인물 (女)"""

    similarity_score_list = []

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

    """ 정상 케이스:신분증과 동일한 인물 (女) """
    def test01_check_sameface_woman_01_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_01.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_01_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test02_check_sameface_woman_01_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_01_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test03_check_sameface_woman_01_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_01_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test04_check_sameface_woman_02_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_02.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_02_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test05_check_sameface_woman_02_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_02_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test06_check_sameface_woman_02_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_02_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test07_check_sameface_woman_03_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_03.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_03_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test08_check_sameface_woman_03_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_03_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test09_check_sameface_woman_03_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_03_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test10_check_sameface_woman_04_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_04.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_04_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test11_check_sameface_woman_04_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_04_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test12_check_sameface_woman_04_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_04_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test13_check_sameface_woman_05_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_05.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_05_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test14_check_sameface_woman_05_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_05_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test15_check_sameface_woman_05_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_05_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test16_check_sameface_woman_06_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_06.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_06_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test17_check_sameface_woman_06_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_06_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test18_check_sameface_woman_06_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_06_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test19_check_sameface_woman_07_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_07.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_07_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test20_check_sameface_woman_07_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_07_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test21_check_sameface_woman_07_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_07_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test22_check_sameface_woman_08_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_08.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_08_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test23_check_sameface_woman_08_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_08_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test24_check_sameface_woman_08_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_08_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test25_check_sameface_woman_09_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_09.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test26_check_sameface_woman_09_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_09_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test27_check_sameface_woman_09_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_09_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test28_check_sameface_woman_10_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_10.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_10_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test29_check_sameface_woman_10_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_10_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test30_check_sameface_woman_10_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_10_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test31_check_sameface_woman_11_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_11.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_11_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test32_check_sameface_woman_11_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_11_2.jpg"
        ios_utils.takeLicense(self, image_path)

    def test33_check_sameface_woman_11_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_11_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test34_check_sameface_woman_12_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_12.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_12_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test35_check_sameface_woman_12_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_12_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test36_check_sameface_woman_12_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_12_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test37_check_sameface_woman_13_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_13.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_13_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test38_check_sameface_woman_13_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_13_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test39_check_sameface_woman_13_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_13_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test40_check_sameface_woman_14_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_14.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_14_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test41_check_sameface_woman_14_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_14_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test42_check_sameface_woman_14_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_14_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test43_check_sameface_woman_15_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_15.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_15_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test44_check_sameface_woman_15_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_15_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test45_check_sameface_woman_15_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_15_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test46_check_sameface_woman_16_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_16.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_16_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test47_check_sameface_woman_16_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_16_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test48_check_sameface_woman_16_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_16_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test49_check_sameface_woman_17_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_17.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_17_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test50_check_sameface_woman_17_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_17_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test51_check_sameface_woman_17_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_17_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test52_check_sameface_woman_18_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_18.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_18_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test53_check_sameface_woman_18_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_18_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test54_check_sameface_woman_18_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_18_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test55_check_sameface_woman_19_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_19.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_19_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test56_check_sameface_woman_19_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_19_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test57_check_sameface_woman_19_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_19_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test58_check_sameface_woman_20_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_20.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_20_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test59_check_sameface_woman_20_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_20_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test60_check_sameface_woman_20_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_20_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test61_check_sameface_woman_21_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_21.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test62_check_sameface_woman_21_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_21_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test63_check_sameface_woman_21_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_21_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test64_check_sameface_woman_22_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_22.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_22_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test65_check_sameface_woman_22_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_22_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test66_check_sameface_woman_22_ark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_22_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test67_check_sameface_woman_23_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_23.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_23_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test68_check_sameface_woman_23_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_23_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test69_check_sameface_woman_23_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_23_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test70_check_sameface_woman_24_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_24.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_24_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test71_check_sameface_woman_24_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_24_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test72_check_sameface_woman_24_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_24_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test73_check_sameface_woman_25_normal(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 일반사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/license/license_woman_25.jpg"
        ios_utils.takeLicense(self, image_path)
        image_path = "ekyc/testData/selfie/selfie_woman_25_1.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test74_check_sameface_woman_25_bright(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 밝게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_25_2.jpg"
        ios_utils.takeSelfie(self, image_path)

    def test75_check_sameface_woman_25_dark(self):
        """본인인증 촬영 테스트 (女): 신분증과 동일한 인물 / 어둡게 촬영된 사진 → 인식률 점수가 0.35이상이고 same face토스트가 표시될 것"""
        image_path = "ekyc/testData/selfie/selfie_woman_25_3.jpg"
        ios_utils.takeSelfie(self, image_path)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
