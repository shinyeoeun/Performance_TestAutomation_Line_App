# coding=utf-8

import unittest
from lib import HTMLTestReport
from sticker.iosStressTest import StressTest


class RunAllScript(object):

    def __init__(self):
        self.test_case_path = "."
        self.title = "Yuki SDK Automation Test Report-iOS"
        self.description = "yuki SDK 스트레스 테스트 스크립트 수행결과레포트"

    def run(self):

        # ToDo 실행 스크립트 지정
        test_suite = unittest.TestSuite()
        test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(StressTest))

        daf = HTMLTestReport.DirAndFiles()

        # ToDo Local용 레포트 생성 패스
        daf.create_dir(title=self.title)
        report_path = HTMLTestReport.GlobalMsg.get_value("report_path")

        # ToDo Jenkins용 레포트 생성 패스
        # daf.set_jenkins_dir("stickerIos")
        # report_path = '/Users/st20073c/lfk_jenkins/workspace/Yuki-Automation_iOS/report/index.html'

        fp = open(report_path, 'wb')
        runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester="LFK: SHIN YEOEUN")
        runner.run(test_suite)
        fp.close()

if __name__ == "__main__":
    RunAllScript().run()
