# test_example.py
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
import time

@pytest.mark.parametrize("udid, systemPort", [
    ("RF8M512ASVM", "8000"),
    ("8BSX1EF7A", "8100"),
]
                         )
def test_sum(udid, systemPort):

    capabilities = {
        'platformName': 'Android',
        'deviceName': 'Genymotion Cloud PaaS',
        'appPackage': 'com.android.chrome',
        'appActivity': 'com.google.android.apps.chrome.Main',
        'udid':udid,
        'systemPort': systemPort,
        'automationName': 'UiAutomator2',
        'noReset': True,
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)

    try:
        time.sleep(10)
    finally:
        driver.quit()
