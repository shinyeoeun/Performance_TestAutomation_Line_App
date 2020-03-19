# coding=utf-8

import unittest
from lib import HTMLTestReport
from ekyc.IosEkycPerfomanceTestMan import IosEkycPerfomanceTestMan
from ekyc.IosEkycPerfomanceTestWoman import IosEkycPerfomanceTestWoman


class RunAllScript(object):

    def __init__(self):
        # ToDo title의 버전 정보 변수화 할 것
        self.test_case_path = "."
        self.title = "ekyc Test Report(iOS) Yuki Demo 2.12.5.1153 "
        self.description = "ekyc yuki Liveness verification service 본인확인 시나리오를 자동으로 수행하는 스크립트" \
                           "■ Test Data: 男性 35名(LFK:30/Clova:5), 女性 25名(LFK:23/Clova:2), Total 60名" \
                           "■ Test Case: https://wiki.linecorp.com/display/linefkqa/Test+Automation+Plan+-+ekyc"

    def run(self):
        test_suite = unittest.TestSuite()

        # ToDo yuki Demo
        test_suite = unittest.TestSuite()
        test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IosEkycPerfomanceTestMan))
        test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IosEkycPerfomanceTestWoman))

        # ToDo Report Path
        # For Jenkins
        #report_path = '/Users/st20073c/lfk_jenkins/workspace/LFK_Yuki_Automation_Test_eKYC_iOS/report/index.html'

        # For Local
        daf = HTMLTestReport.DirAndFiles()
        daf.create_dir(title=self.title)
        report_path = HTMLTestReport.GlobalMsg.get_value("report_path")

        fp = open(report_path, 'wb')
        runner = HTMLTestReport.HTMLTestRunner(stream=fp, title=self.title, description=self.description, tester="shin")
        runner.run(test_suite)
        fp.close()


if __name__ == "__main__":
    RunAllScript().run()
