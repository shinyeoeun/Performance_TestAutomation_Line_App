"""
pytest로 여러 디바이스에서 동시에 테스트 스크립트를 돌리는 방법
"""

# test_example.py
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
import time

# 테스트 디바이스의 udid와 system port를 정의함(여기서는 Galaxy s10, Galaxy Note 7 2대로 테스트)
@pytest.mark.parametrize("udid, system_port, device_name", [
    ("R58M46AFQGD", "8212", "Samsung Galaxy S10"), ])

# 테스트 메소드의 파라미터로 위에서 정의한 udid, systemport를 넘겨주고 capabilities값에 매핑해줌
def test_main(udid, system_port, device_name):
    capabilities = {
        'platformName': 'Android',
        'platformVersion': '9',
        'udid': udid,
        'deviceName': device_name,
        'appPackage': "jp.naver.line.android",
        'appActivity': '.activity.SplashActivity',
        'automationName': 'UiAutomator2',
        'systemPort': system_port,
        'noReset': True,
        'newCommandTimeout': '180',
        'clearDeviceLogsOnStart': True,
    }

    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)

# 여기서부터 테스트 스탭을 작성함
    try:
        time.sleep(10)
    finally:
        driver.quit()
