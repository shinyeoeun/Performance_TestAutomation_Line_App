#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from utils import android_utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
import matplotlib.pyplot as plt
from pyecharts.charts import Bar
from pyecharts import options
from pyecharts.charts import Line
from pyecharts.globals import ThemeType

class AndroidPerformanceTest(unittest.TestCase):
    """ 테스트카테고리: Yuki QA Automation """

    MEMORY = []
    MEMORY_PSS_TOTAL_VALUE = []
    MEMORY_PSS_TOTAL_VALUE_LIST = []

    CPU = []
    CPU_VALUE = []
    CPU_VALUE_LIST = []

    TIME_SEC = []

    STICKER_LIST_FIRST = ["61609", "62141", "61958", "62638", "60847"]
    STICKER_LIST_SECOND = []
    SWIPE_DURATION_DEFAULT = 2700  # Swipe 시간 기본값
    CATEGORY_INDEX = 8  # 카테고리 인덱스

    TIME_OUT = 10
    PKG = "com.linecorp.yuki"

    def test001_get_performance_data_61609(self):
        """ 스티커 적용상태에서 리소스 최소값/최대값 측정: 61609"""
        print("[LOG]=============== TEST START")

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['newCommandTimeout'] = '180'
        desired_caps['deviceName'] = 'Galaxy S10'
        desired_caps['appPackage'] = self.PKG
        desired_caps['appActivity'] = '.EffectDemoActivity'
        desired_caps['udid'] = 'RF8M512ASVM'
        desired_caps['noReset'] = 'true'
        desired_caps['clearDeviceLogsOnStart'] = 'true'
        desired_caps['systemPort'] = 8212
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.screenX = self.driver.get_window_size().get("width")
        self.screenY = self.driver.get_window_size().get("height")
        self.wait = WebDriverWait(self.driver, 20)

        # yuki-Demo 메뉴 > Camera Tap
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Camera(Integration)")').click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/face_sticker_button')))

        # Target Category 탭
        self.driver.find_element_by_id("com.linecorp.yuki:id/face_sticker_button").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'com.linecorp.yuki:id/sticker_category_view')))
        self.driver.swipe(self.screenX * 0.9, self.screenY * 0.98, self.screenX * 0.1, self.screenY * 0.98, self.SWIPE_DURATION_DEFAULT)
        android_utils.tapTargetCategory(self, int(self.CATEGORY_INDEX))
        self.driver.back()
        self.driver.find_element_by_id("com.linecorp.yuki:id/qa_play_button").click()

        for index in range(len(self.STICKER_LIST_FIRST)):
            # 스티커 하나씩 탭
            self.driver.find_element_by_id("com.linecorp.yuki:id/face_sticker_button").click()
            TouchAction(self.driver).tap(self.driver.find_element_by_android_uiautomator('new UiSelector().text("' + self.STICKER_LIST_FIRST[index] + '")')).perform()
            self.driver.back()

            # 10초간 CPU/Memory 측정
            for i in range(10):
                # now = datetime.now()
                # self.TIME_SEC.append("%s:%s" % (now.minute, now.second))
                dt = datetime.datetime.now()
                self.TIME_SEC.append(dt.strftime("%M %S"))
                self.MEMORY_LIST = self.driver.get_performance_data(self.PKG, "memoryinfo", self.TIME_OUT)
                self.MEMORY_PSS_TOTAL_VALUE = self.MEMORY_LIST[1]
                self.MEMORY_PSS_TOTAL_VALUE_LIST.append(int(self.MEMORY_PSS_TOTAL_VALUE[5]))
                #self.CPU = self.driver.get_performance_data(self.PKG, 'cpuinfo', 5)

                time.sleep(1)

        self.driver.swipe(self.screenX * 0.5, self.screenY * 0.8, self.screenX * 0.5, self.screenY * 0.85, self.SWIPE_DURATION_DEFAULT)
        self.driver.quit()

        # 그래프 작성
        x = self.TIME_SEC
        y = self.MEMORY_PSS_TOTAL_VALUE_LIST
        #self.CPU.append(os.popen("adb shell top -n 1 | findstr com.linecorp.yu+").readline().split()[9].strip(' '))
        #self.CPU.append(os.popen("adb shell top -n 1 | findstr com.linecorp.yu+").readline().split()[9].strip(' ').split(".")[0])
        #print(self.CPU)
        print(x)
        print(y)

        # plot
        plt.plot(x, y, color='blue')
        plt.style.use(['ggplot'])
        plt.title('RAM Usage')

        plt.ylabel("memory:Total PSS(KB)")
        plt.xlabel('time(s)')
        plt.grid(True)
        plt.xticks(fontsize=9, rotation=90)
        plt.show()

        """
        line = Line(init_opts=options.InitOpts(theme=ThemeType.LIGHT)).set_global_opts().set_global_opts(title_opts=options.TitleOpts(title="yuki sdk RAM usage", subtitle="yuki sdk Automation 카테고리 스티커 적용중 RAM사용량 측정 결과 "))

        line.add_xaxis(x)
        line.add_yaxis("Total PSS(KB)", y, markline_opts=options.MarkLineOpts(data=[options.MarkLineItem(type_="average")]))
        line.render("yuki.html")


        bar = (
            Bar()
                .add_xaxis(x)
                .add_yaxis("Total PSS (KB)", y, markline_opts = options.MarkLineOpts(data=[options.MarkLineItem(type_="average")]))
                .set_global_opts(title_opts=options.TitleOpts(title="yuki sdk RAM 사용량 측정 결과"))
                .set_series_opts(
                label_opts=options.LabelOpts(is_show=False),
                markpoint_opts=options.MarkPointOpts(
                    data=[
                        options.MarkPointItem(type_="max", name="최대값"),
                        options.MarkPointItem(type_="min", name="최소값"),
                    ]
                ),
            )
        )
        bar.render()
        """

if __name__ == '__main__':
    unittest.main(warnings='ignore')
    unittest.main()

