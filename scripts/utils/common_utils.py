# -*- coding: utf-8 -*-
import os
import time
import cv2
import imagehash
import numpy as np
from PIL import Image
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import subprocess
import platform

def get_toast_text(self, text, timeout=5, poll_frequency=0.01):
    """이미지를 화면에 출력

    Parameters
    ----------
    text : string
        toast에 표시되는 문자열
    timeout : int
        타임아웃 되기까지 대기하는 시간
    poll_frequency : float
        다음 호출까지의 간격
    -------

    Returns
    -------
    String
        toast에 출력된 문자열

    Examples
    --------
    >>> get_toast_text("face recognize fail")
        "face recognize fail"
    """
    toast_element = (By.XPATH, "//*[contains(@text, " + "'" + text + "'" + ")]")
    toast = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_element))
    return toast.text


def closeApplication():
    """스크립트를 실핸한 OS를 판별하여, 각 OS에 해당하는 image viewer application의 테스크를 종료하는 메소드

    Return
    ----------
    command:
        windows의 경우 taskkill 커맨드를, mac의 경우 osascript 커맨드를 실행
    """
    if platform.system() == "Windows":
        return os.system('taskkill /f /im Microsoft.Photos.exe')
    elif platform.system() == "Darwin":
        return subprocess.call(['osascript', '-e', 'tell application "Preview" to quit'])


def getImage(path):
    """이미지를 화면에 출력하는 메소드

    Parameters
    ----------
    path : String
        불러올 이미지의 경로
    """
    img = Image.open(path)
    img.show()
    time.sleep(4)


def getScreenshot(self, filename, path):
    """디바이스의 스크린샷 취득하여 지정한 패스에 png파일로 저장

    Parameters
    ----------
    filename : string
        파일명(png)
    path : string
        파일을 저장할 패스
    -------

    Examples
    --------
    >>> getScreenshot("image1", "\Documents\Dev\yukiTestAutomation\")
    """
    self.driver.get_screenshot_as_file(path + "/" + filename + ".png")

def frame2dhash(self, frame):
    img = Image.fromarray(np.uint8(frame))
    return imagehash.dhash(img)


def get_all_dhashes(self, mov):
    dhashes = []
    while 1:
        ret, frame = mov.read()
        if not ret: break
        dhashes.append(frame2dhash(self, frame))
    return dhashes


def get_random_points_dhashes(self, mov, points=1):
    """
    영상의 시작점/끝점, 랜덤점의 프레임을 dhash화 하여 배열로서 반환

    Parameters
    ----------
    mov : int
        영상
    points : int
        랜덤 N점

    Returns
    -------
    list:
        영상에서 랜덤으로 추출한 프레임 리스트
    """
    _, frame = mov.read()
    dhashes = [frame2dhash(self, frame)]

    if points > 0:
        num_frames = mov.get(cv2.CAP_PROP_FRAME_COUNT) - 2
        max_skip = int(num_frames / points)

        for point in range(points):
            skips = randint(1, max_skip)
            for _ in range(skips - 1):
                _ = mov.read()
            _, frame = mov.read()
            dhashes.append(frame2dhash(self, frame))

    pre_frame = None
    ret = True
    while ret:
        pre_frame = frame
        ret, frame = mov.read()
    dhashes.append(frame2dhash(self, pre_frame))

    return dhashes

def get_movincp(self, originPath, targetPath, points=3):
    origin = cv2.VideoCapture(originPath)
    target = cv2.VideoCapture(targetPath)

    origin_dhashes = get_random_points_dhashes(self, origin, points)
    target_dhashes = get_all_dhashes(self, target)
    target_index = 0
    distances = []

    for origin_dhash in origin_dhashes:
        min_distance = 64
        for i in range(target_index, len(target_dhashes)):
            target_dhash = target_dhashes[i]
            distance = origin_dhash - target_dhash
            if distance < min_distance:
                min_distance = distance
                target_index = i + 1
        distances.append(min_distance)

    return (64 - np.array(distances).mean()) / 64

def get_movincb(self, originPath, targetPath, points=1, threshold=1):
    origin = cv2.VideoCapture(originPath)
    target = cv2.VideoCapture(targetPath)

    origin_dhashes = get_random_points_dhashes(self, origin, points)
    origin_dhash = origin_dhashes.pop(0)
    while 1:
        ret, frame = target.read()
        if not ret:
            break
        target_dhash = frame2dhash(self, frame)
        if origin_dhash - target_dhash <= threshold:
            if len(origin_dhashes) > 0:
                origin_dhash = origin_dhashes.pop(0)
            else:
                return "Pass"
    return "Fail"


