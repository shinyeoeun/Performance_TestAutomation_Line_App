# coding=utf-8

import unittest
from lib import HTMLTestReport
from sticker.AndroidPerformanceTest import AndroidPerformanceTest

class RunAllScript(object):

    def __init__(self):
        # ToDo title의 버전 정보 변수화 할 것
        self.test_case_path = "."
        self.title = "Yuki SDK Automation Test Report-Android (2.16.1.1421)"
        self.description = "yuki SDK 리그레션테스트케이스 스크립트 수행결과레포트"

    def run(self):
        # ToDo 실행 스크립트 지정
        test_suite = unittest.TestSuite()
        test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AndroidPerformanceTest))

        daf = HTMLTestReport.DirAndFiles()

        # ToDo Local용 레포트 생성 패스
        daf.create_dir(title=self.title)
        report_path = HTMLTestReport.GlobalMsg.get_value("report_path")

        # ToDo Jenkins용 레포트 생성 패스
        # daf.set_jenkins_dir("stickerAndroid")
        # report_path = '/Users/st20073c/lfk_jenkins/workspace/LFK_Yuki_Automation_Test_sticker_Android/report/index.html'

        fp = open(report_path, 'wb')
        runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester="LFK: SHIN YEOEUN", build="2.16.1.1421")
        runner.run(test_suite)
        fp.close()

if __name__ == "__main__":
    RunAllScript().run()
