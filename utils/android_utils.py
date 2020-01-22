# -*- coding: utf-8 -*-
import time

SWIPE_DURATION_DEFAULT = 700  # Swipe 기본값
FILE_PATH_FOR_TEST_RESULT = "sticker/video/TestResult/"  # 테스트 결과영상 저장 패스

"""
디바이스 화면 녹화
"""
def recordDeviceScreen(self, record_time):
    time.sleep(1)
    self.driver.start_recording_screen()
    time.sleep(record_time)
    payload = self.driver.stop_recording_screen()
    with open(FILE_PATH_FOR_TEST_RESULT + "_result.mp4", "wb") as fd:
        import base64
        fd.write(base64.b64decode(payload))

"""
log의 첫번째 10라인과 마지막 10라인을 출력
"""
def capture_logcat(self):
    logs = self.driver.get_log('logcat')
    log_messages = list(map(lambda log: log['message'], logs))
    print('\n'.join(log_messages[:10]))
    print('...')
    print('\n'.join(log_messages[-9:]))

def tapTargetCategory(self, index):
    sticker_parent = self.driver.find_element_by_id("com.linecorp.yuki:id/sticker_category_view")
    sticker_children = sticker_parent.find_elements_by_class_name("android.widget.FrameLayout")
    sticker_children[index].find_element_by_class_name("android.widget.FrameLayout").click()

def tapTargetSticker(self, sticker_id):
    self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+sticker_id+'")').click()
    self.driver.back()
