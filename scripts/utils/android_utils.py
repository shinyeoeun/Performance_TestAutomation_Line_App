# -*- coding: utf-8 -*-
import time
from utils import common_utils

SWIPE_DURATION_DEFAULT = 700  # Swipe 기본값
FILE_PATH_FOR_TEST_RESULT = "sticker/video/TestResult/"  # 테스트 결과영상 저장 패스
#FILE_PATH_FOR_TEST_RESULT = "sticker/video/ExpectedResult/"  # 테스트 결과영상 저장 패스

"""
動画録画/디바이스 화면 녹화
str sticker ID
int 録画時間(sec)/녹화시간(sec)
"""
def recordDeviceScreen(self, sticker_id, record_time):
    time.sleep(1)
    self.driver.start_recording_screen()
    time.sleep(record_time)
    payload = self.driver.stop_recording_screen()
    with open(FILE_PATH_FOR_TEST_RESULT + sticker_id + "_result.mp4", "wb") as fd:
        import base64
        fd.write(base64.b64decode(payload))

def getVideoSmilarity(self, sticker_id):
    print("[LOG] Compare「" + sticker_id + "_android.mp4」to「" + sticker_id + "_result.mp4」")
    similarity_score = common_utils.get_movincp(self, "sticker/video/ExpectedResult/"+sticker_id+"_android.mp4", "sticker/video/TestResult/"+sticker_id+"_result.mp4")
    return similarity_score

# log의 첫번째 10라인과 마지막 10라인을 출력
def capture_logcat(self):
    logs = self.driver.get_log('logcat')
    log_messages = list(map(lambda log: log['message'], logs))
    print('\n'.join(log_messages[:10]))
    print('...')
    print('\n'.join(log_messages[-9:]))

def switchShowDebugLog(self):
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.Switch").click()
    self.driver.find_element_by_id("com.linecorp.yuki:id/menu_done").click()
    time.sleep(3)

"""
def recordClipmovie(self, recordtime, stickerId, path):
    # 비디오 메뉴 탭
    video_btn = (By.ID, 'com.linecorp.yuki:id/camera_mode_video')
    WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located(video_btn))
    self.driver.find_element_by_id("com.linecorp.yuki:id/camera_mode_video").click()

    # 녹화시작
    record_btn = (By.ID, 'com.linecorp.yuki:id/record_animation')
    WebDriverWait(self.driver, 30, 1).until(EC.presence_of_element_located(record_btn))
    self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation").click()
    # 녹화
    time.sleep(int(recordtime))
    # 녹화 정지
    self.driver.find_element_by_id("com.linecorp.yuki:id/record_animation").click()

    # 단말에서 파일 로컬로 가져오고 단말 내 파일 삭제
    filenameFromDevice = os.popen("adb shell ls /sdcard/DCIM/LINE")
    os.popen("adb pull /sdcard/DCIM/LINE/" + filenameFromDevice + ".mp4 " + path)
    os.popen("adb shell rm -rf /sdcard/DCIM/LINE/" + filenameFromDevice)  # 파일 삭제

    # 파일 이름 변경
    filename = "sticker_" + stickerId
    os.rename("C://yukiSDK/video/TestResult" + filenameFromDevice, "C://yukiSDK/video/TestResult" + filename)
"""

"""
Stickerのカテゴリ指定 ＆ click/Sticker 카테고리 지정 ＆ click
srt sticker_category_view > Framelayoutのindex/sticker_category_view > Framelayout의 index
"""
def tapTargetCategory(self, index):
    sticker_parent = self.driver.find_element_by_id("com.linecorp.yuki:id/sticker_category_view")
    sticker_children = sticker_parent.find_elements_by_class_name("android.widget.FrameLayout")
    sticker_children[index].find_element_by_class_name("android.widget.FrameLayout").click()

"""
Stickerカテゴリ内のStickerを指定 ＆ click/Sticker 카테고리내의 Sticker를 지정 ＆ click
int list_view_sticker > Framelayoutのindex/list_view_sticker > Framelayout의 index
"""
def tapTargetSticker(self, sticker_id):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+sticker_id+'")').click()
    self.driver.back()

def takeLicense(self, image_path):
    """이미지를 화면에 출력

    Parameters
    ----------
    text : string
        토스트에 표시되는 문자열
    timeout : int
        타임아웃 되기까지 대기하는 시간
    poll_frequency : float
        다음 호출간의 간격시간
    -------

    Returns
    -------
    String
        토스트 문자열

    Examples
    --------
    >>> get_toast_text("face recognize fail")
        "face recognize fail"
    """
    print("[LOG]test start")
    print("[LOG]image path: " + image_path)
    # 신분증 사진 표시
    common_utils.getImage(image_path)
    time.sleep(3)
    # 촬영버튼 탭
    self.driver.find_element_by_id("com.linecorp.YukiDemo:id/face_1_button").click()
    # 사진 종료
    common_utils.closeApplication()

def takeSelfie(self, image_path):
    """이미지를 화면에 출력

    Parameters
    ----------
    path : String
        이미지 패스
    -------
    """
    print("[LOG]image path: " + image_path)
    # 셀카사진 표시
    common_utils.getImage(image_path)
    time.sleep(2)
    # 촬영버튼 탭
    self.driver.find_element_by_id("com.linecorp.YukiDemo:id/face_2_button").click()
    time.sleep(2)
    # 스크린샷 저장
    self.daf.get_screenshot(self.driver)
    # 인식률 취득 및 결과판정 + 통계용 리스트 값 추가
    similarity_score = self.driver.find_element_by_id("com.linecorp.YukiDemo:id/similarity_display").get_attribute(
        "text")
    self.assertTrue(float(similarity_score) >= 0.35, "[LOG]  similarity_score: " + similarity_score)
    self.similarity_score_list.append(similarity_score)
    # 사진 종료
    common_utils.closeApplication()
    print("[LOG] similarity_score: " + similarity_score)

def setTestVideo(self, test_video_title):
    self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[16]").click()
    time.sleep(2)
    # sdcard 영상 중 AR용 영상 적용
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+test_video_title+'")').click()
    time.sleep(1)
    # Debug Menu 변경사항 저장
    self.driver.find_element_by_id("com.linecorp.yuki:id/menu_done").click()
    # 영상 재생버튼 요소가 리프레쉬 되지 않는 현상 해결을 위해 락,언락 처리 수행
    self.driver.lock(1)
    self.driver.unlock()
    time.sleep(3)