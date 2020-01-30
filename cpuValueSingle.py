#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from appium import webdriver
import time
import matplotlib.pyplot as plt
from threading import Thread
import numpy as np
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from pylab import *

CPU = []
CPU_LIST = []
TIME_SEC = []
CPU_VALUE_LIST = []
CPU_VALUE = []

def getRawData(self, TIME_SEC, CPU):
    RAW_DATA = pd.DataFrame({'Time': TIME_SEC, 'RAM Usage(Total PSS(KB))': self.CPU_VALUE_LIST}, columns=['Time', 'CPU'])
    RAW_DATA.to_csv("sssss.csv", index=False)
    return RAW_DATA


def getCurrentTime(self):
    currentTime = time.strftime("%H:%M:%S")
    return currentTime


def generateGraph(self):
    print(self.CPU)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks(np.arange(len(self.CPU)))
    ax.set_xticklabels(self.STICKER_ID_LIST, rotation=45)
    ax.set_title('Yuki SDK CPU Usag:Total PSS(KB)')
    ax.set_ylabel('Total PSS(KB)')
    ax.set_xlabel('Sticker ID')
    ax.plot(self.CPU)
    plt.show()

def getRawDataCpu(TIME_SEC, CPU_VALUE_LIST):
    RAW_DATA = pd.DataFrame({'Time': TIME_SEC, 'cpu': CPU_VALUE_LIST}, columns=['Time', 'cpu'])
    RAW_DATA.to_csv("yuki_cpu_raw_data.csv", index=False)


if __name__ == '__main__':
    print("[LOG]=============== resource measurement start ===============")
    for index in range(30):
        TIME_SEC.append(time.strftime("%H:%M:%S"))
        CPU_LIST = os.popen("adb shell top -n 1 | findstr com.linecorp.yu+").readline().split()[8]
        CPU_VALUE_LIST.append(int(CPU_LIST[0:2]))
        print("[LOG] CPU data: " + CPU_LIST[0:2])
    print("[LOG]=============== resource measurement end ===============")

    getRawDataCpu(TIME_SEC, CPU_VALUE_LIST)

