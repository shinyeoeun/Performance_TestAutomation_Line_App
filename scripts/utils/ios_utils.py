# -*- coding: utf-8 -*-
import time
from utils import common_utils

########## for ekyc
def takeLicense(self, image_path):
    print("[LOG] TestCase Stated")
    print("[LOG]image path: " + image_path)
    # 신분증 사진 표시
    common_utils.getImage(image_path)
    time.sleep(2)
    # 셀카 촬영
    self.driver.find_element_by_accessibility_id("default").click()
    time.sleep(1)
    # 사진 종료
    common_utils.closeApplication()

def takeSelfie(self, image_path):
    print("[LOG]image path: " + image_path)
    # 셀카 사진 표시
    common_utils.getImage(image_path)
    time.sleep(2)
    # 셀카 촬영
    self.driver.find_element_by_accessibility_id("target").click()
    time.sleep(2)
    # 스크린샷 저장
    self.daf.get_screenshot(self.driver)
    # 인식률 취득 및 결과판정 + 통계용 리스트 값 추가
    similarity_score = self.driver.find_element_by_xpath(
        "//XCUIElementTypeApplication[@name='YukiCameraDemo']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextView").get_attribute(
        "value")
    self.assertTrue(float(similarity_score) > 0.35, "[LOG]  similarity_score: " + similarity_score)
    # 사진 종료
    common_utils.closeApplication()
    print("[LOG] similarity_score: " + similarity_score)

########## for sticker
def getVideoSmilarity(self, sticker_id):
    print("[LOG] Compare「" + sticker_id + "_ios.mp4」to「" + sticker_id + "_result.mp4」")
    similarity_score = common_utils.get_movincp(self
                                   , "sticker/video/ExpectedResult/"+sticker_id+"_ios.mp4"
                                   , "sticker/video/TestResult/"+sticker_id+"_result.mp4")

    return similarity_score
