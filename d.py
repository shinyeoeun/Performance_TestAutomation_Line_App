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

def getRawData(self, TIME_SEC, CPU):
    RAW_DATA = pd.DataFrame({'Time': TIME_SEC, 'RAM Usage(Total PSS(KB))': self.CPU_VALUE_LIST},
                            columns=['Time', 'CPU'])
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


if __name__ == '__main__':
    print("[LOG]=============== resource measurement start ===============")
    for index in range(10):
        # CPU = driver.get_performance_data(PACKAGE, 'cpuinfo', 5)

        # CPU.append(os.popen("adb shell top -n 1 | findstr com.linecorp.yu+").readline().split()[9].strip(' '))
        CPU.append(os.popen("adb shell top -n 1 | findstr com.linecorp.yu+").readline().split()[9].strip(' '))

        print("[LOG] CPU data: " + CPU[index])
    print("[LOG]=============== resource measurement end ===============")
