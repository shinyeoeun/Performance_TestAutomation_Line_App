# coding=utf-8

import datetime
import io
import subprocess
import time
import unittest
from xml.sax import saxutils
import sys
import os
import re
import platform

# 全局变量      -- Gelomen
_global_dict = {}


# 让新建的报告文件夹路径存入全局变量       -- Gelomen
class GlobalMsg(object):
    def __init__(self):
        global _global_dict
        _global_dict = {}

    @staticmethod
    def set_value(name, value):
        _global_dict[name] = value

    @staticmethod
    def get_value(name):
        try:
            return _global_dict[name]
        except KeyError:
            return None


# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to sys.stdout and sys.stderr are automatically captured. However
# in some cases sys.stdout is already cached before HTMLTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
#   >>>


class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


# ----------------------------------------------------------------------
# Template


class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.

    Overall structure of an HTML report

    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: 'Pass',
        1: 'Fail',
        2: 'Error',
    }

    DEFAULT_TITLE = 'Default Title'
    DEFAULT_DESCRIPTION = ''
    DEFAULT_TESTER = 'QA'
    DEFAULT_BUILD = 'x.xx.x'

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    <script src="https://img.hcharts.cn/highcharts/highcharts.js"></script>
    <script src="https://img.hcharts.cn/highcharts/modules/exporting.js"></script>
    %(stylesheet)s
</head>
<body >
<script language="javascript" type="text/javascript">

    $(function(){
        // 修改 失败 和 错误 用例里对应按钮的颜色ClassName为动态加载 -- Gelomen
    	$("button").each(function () {
    	    var text = $(this).text();
    	    if(text == ""){
    	        $(this).addClass("btn-danger")
            }else if(text == "Error") {
                $(this).addClass("btn-warning")
            }
        });

        // 给失败和错误合集加样式 -- Gelomen
        var p_attribute = $("p.attribute");
        p_attribute.eq(4).addClass("failCollection");
        p_attribute.eq(5).addClass("errorCollection");

        // 打开截图，放大，点击任何位置可以关闭图片  -- Gelomen
        $(".screenshot").click(function(){
            var img = $(this).attr("img");
            $('.pic_show img').attr('src', img);
            $('.pic_looper').fadeIn(200);
            $('.pic_show').fadeIn(200);

            var browserHeight = $(window).height();
            var pic_boxHeight = $(".pic_box").height();
            var top = (browserHeight - pic_boxHeight)/2;
            $('.pic_box').css("margin-top", top + "px")

        });
        $('.pic_looper, .pic_show').click(function(){
            $('.pic_looper').fadeOut(200);
            $('.pic_show').fadeOut(200)
        });

        var browserWidth = $(window).width();
        var margin_left = browserWidth/2 - 450;
        if(margin_left <= 240){
            $("#container").css("margin", "auto");
        }else {
            $("#container").css("margin-left", margin_left + "px");
        }

        $(window).resize(function(){
            // 改变窗口大小时，自动改变图片与顶部的距离  -- Gelomen
            var browserHeight = $(window).height();
            var pic_boxHeight = $(".pic_box").height();
            var top = (browserHeight - pic_boxHeight)/2;
            $('.pic_box').css("margin-top", top + "px");


            // 改变窗口大小时，自动改变饼图的边距  -- Gelomen
            var browserWidth = $(window).width();
            var margin_left = browserWidth/2 - 450;
            if(margin_left <= 240){
                $("#container").css("margin", "auto");
            }else {
                $("#container").css("margin-left", margin_left + "px");
            }
        });

        // 距离顶部超过浏览器窗口一屏时，回到顶部按钮才出现  -- Gelomen
        $(window).scroll(function(){
            var browserHeight = $(window).height();
            var top = $(window).scrollTop();
            if(top >= browserHeight){
                $("#toTop").css("display", "block")
            }else {
                $("#toTop").css("display", "none")
            }
        })

        // 增加回到顶部过程的动画，以看上去不会那么生硬  -- Gelomen
        $("#toTop").click(function() {
            $("html,body").animate({"scrollTop":0}, 700)
        })

        // 增加饼状图  -- Gelomen
        $('#container').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                spacing : [0, 0, 0, 0]
            },
            credits: {
                enabled: false
            },
            navigation: {
                buttonOptions: {
                    enabled: false
                }
            },
            title: {
                floating:true,
                text: 'Test result ratio'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    colors: ['#81ca9d', '#f16d7e', '#fdc68c'],
                    dataLabels: {
                        enabled: true,
                        format: '<b>{point.name}</b>: {point.percentage:.1f} %%',
                        style: {
                            color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                        }
                    },
                    point: {
                        events: {
                            mouseOver: function(e) {  // 鼠标滑过时动态更新标题
                                chart.setTitle({
                                    text: e.target.name+ '\t'+ e.target.y
                                });
                            }
                        }
                    }
                }
            },
            series: [{
                type: 'pie',
                innerSize: '80%%',
                name: 'rate',
                data: [
                    ['Pass', %(Pass)s],
                    {
                        name: 'Fail',
                        y: %(fail)s,
                        sliced: true,
                        selected: true
                    },
                    ['Error', %(error)s]
                ]
            }]
        }, function(c) {
            // 环形图圆心
            var centerY = c.series[0].center[1],
                titleHeight = parseInt(c.title.styles.fontSize);
            c.setTitle({
                y:centerY + titleHeight/2
            });
            chart = c;
        });

        // 查看 失败 和 错误 合集链接文字切换  -- Gelomen
        $(".showDetail").click(function () {
            if($(this).html() == "Open"){
                $(this).html("Close")
            }else {
                $(this).html("Open")
            }
        })
    });


output_list = Array();

/*level 调整增加只显示通过用例的分类 --Findyou / 修复筛选显示bug --Gelomen
0:Summary //all hiddenRow
1:Failed  //pt&et hiddenRow, ft none
2:Pass    //pt none, ft&et hiddenRow
3:Error   //pt&ft hiddenRow, et none
4:All     //all none
*/
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level == 2 || level == 0 || level == 3) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
                // 切换筛选时只显示预览   -- Gelomen
                $("div[id^='div_ft']").attr("class", "collapse");
                $("div[id^='div_et']").attr("class", "collapse");
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level == 1 || level == 0 || level == 3) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
                // 切换筛选时只显示预览   -- Gelomen
                $("div[id^='div_ft']").attr("class", "collapse");
                $("div[id^='div_et']").attr("class", "collapse");
            }
        }
        if (id.substr(0,2) == 'et') {
            if (level == 1 || level == 0 || level == 2) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
                // 切换筛选时只显示预览   -- Gelomen
                $("div[id^='div_ft']").attr("class", "collapse");
                $("div[id^='div_et']").attr("class", "collapse");
            }
        }
    }

    //加入【详细】切换文字变化 --Findyou
    detail_class=document.getElementsByClassName('detail');
	//console.log(detail_class.length)
	if (level == 3) {
		for (var i = 0; i < detail_class.length; i++){
			detail_class[i].innerHTML="Close"
		}
	}
	else{
			for (var i = 0; i < detail_class.length; i++){
			detail_class[i].innerHTML="Detail"
		}
	}
}

function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        //ID修改 点 为 下划线 -Findyou
        tid0 = 't' + cid.substr(1) + '_' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
            if (!tr) {
                tid = 'e' + tid0;
                tr = document.getElementById(tid);
            }
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        //修改点击无法收起的BUG，加入【详细】切换文字变化 --Findyou
        if (toHide) {
            document.getElementById(tid).className = 'hiddenRow';
            document.getElementById(cid).innerText = "Detail"
        }
        else {
            document.getElementById(tid).className = '';
            document.getElementById(cid).innerText = "Close"
        }
    }
}

function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>
%(heading)s
%(report)s
%(ending)s

</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: Mangal;padding: 20px; font-size: 150%; }
table       { font-size: 12px; }
.table tbody tr td{
            vertical-align: middle;
        }

/* -- heading ---------------------------------------------------------------------- */
.heading .description, .attribute {
    clear: both;
}

/* --- 失败和错误合集样式 -- Gelomen --- */
.failCollection, .errorCollection {
    width: 100px;
    float: left;
}
#failCaseOl li {
    color: red
}
#errorCaseOl li {
    color: orange
}

/* --- 打开截图特效样式 -- Gelomen --- */
.data-img{
    cursor:pointer
}

.pic_looper{
    width:100%;
    height:100%;
    position: fixed;
    left: 0;
    top:0;
    opacity: 0.6;
    background: #000;
    display: none;
    z-index: 100;
}

.pic_show{
    width:100%;
    position:fixed;
    left:0;
    top:0;
    right:0;
    bottom:0;
    margin:auto;
    text-align: center;
    display: none;
    z-index: 100;
}

.pic_box{
    padding:10px;
    width:90%;
    height:90%;
    margin:40px auto;
    text-align: center;
    overflow: hidden;
}

.pic_box img{
    width: auto;
    height: 100%;
    -moz-box-shadow: 0px 0px 20px 0px #000;
    -webkit-box-shadow: 0px 0px 20px 0px #000;
    box-shadow: 0px 0px 20px 0px #000;
}

/* --- 饼状图div样式 -- Gelomen --- */
#container {
    width: 450px;
    height: 300px;
    float: left;
}

/* -- report ------------------------------------------------------------------------ */
#total_row  { font-weight: bold; }
.passCase   { color: #5cb85c; }
.failCase   { color: #d9534f; font-weight: bold; }
.errorCase  { color: #f0ad4e; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
.screenshot:link { text-decoration: none;color: deeppink; }
.screenshot:visited { text-decoration: none;color: deeppink; }
.screenshot:hover { text-decoration: none;color: darkcyan; }
.screenshot:active { text-decoration: none;color: deeppink; }
</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    # 添加显示截图 和 饼状图 的div  -- Gelomen
    HEADING_TMPL = """<div class='pic_looper'></div> <div class='pic_show'><div class='pic_box'><img src=''/></div> </div>
<div class='heading'>
<div style="width: 650px; float: left;">
    <h1 style="font-family: Mangal">%(title)s</h1>
    %(parameters)s
    <p class='description'>%(description)s</p>
</div>
<div id="container"></div>
</div>

"""  # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s : </strong> %(value)s</p>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #
    # 汉化,加美化效果 --Findyou
    REPORT_TMPL = """
<div style="width: 500px; clear: both;">
<p id='show_detail_line'>
<a class="btn btn-primary" href='javascript:showCase(0)'>Sum{ %(passrate)s }</a>
<a class="btn btn-success" href='javascript:showCase(2)'>pass{ %(Pass)s }</a>
<a class="btn btn-danger" href='javascript:showCase(1)'>fail{ %(fail)s }</a>
<a class="btn btn-warning" href='javascript:showCase(3)'>error{ %(error)s }</a>
<a class="btn btn-info" href='javascript:showCase(4)'>All{ %(count)s }</a>
</p>
</div>
<table id='result_table' class="table table-condensed table-bordered table-hover">
<colgroup>
<col align='left' style="width: 300px;"/>
<col align='right' style="width: 300px;"/>
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' style="width: 200px;"/>
</colgroup>
<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
    <td>Test Title</td>
    <td>Test Description</td>
    <td>Total</td>
    <td>Passed</td>
    <td>Failed</td>
    <td>Error</td>
    <td>Time</td>
    <td>Detail</td>
</tr>
%(test_list)s
<tr id='total_row' class="text-center active">
    <td colspan='2'>Total</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>%(time_usage)s</td>
    <td>Passing rate：%(passrate)s</td>
</tr>
</table>
"""  # variables: (test_list, count, Pass, fail, error ,passrate)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s warning'>
    <td>%(name)s</td>
    <td>%(doc)s</td>
    <td class="text-center">%(count)s</td>
    <td class="text-center">%(Pass)s</td>
    <td class="text-center">%(fail)s</td>
    <td class="text-center">%(error)s</td>
    <td class="text-center">%(time_usage)s</td>
    <td class="text-center"><a href="javascript:showClassDetail('%(cid)s',%(count)s)" class="detail" id='%(cid)s'>Detail</a></td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    # 失败 的样式，去掉原来JS效果，美化展示效果  -Findyou / 美化类名上下居中，有截图列 -- Gelomen
    REPORT_TEST_WITH_OUTPUT_TMPL_1 = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s' style="vertical-align: middle"><div class='testcase'>%(name)s</div></td>
    <td style="vertical-align: middle">%(doc)s</td>
    <td colspan='5' align='center'>
    <!--默认收起错误信息 -Findyou
    <button id='btn_%(tid)s' type="button"  class="btn btn-xs collapsed" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
    <div id='div_%(tid)s' class="collapse">  -->

    <!-- 默认展开错误信息 -Findyou /  修复失败按钮的颜色 -- Gelomen -->
    <button id='btn_%(tid)s' type="button"  class="btn btn-xs" data-toggle="collapse" data-target='#div_%(tid)s,#div_%(tid)s_screenshot'>%(status)s</button>
    <div id='div_%(tid)s' class="collapse in">
    <pre style="text-align:left">
    %(script)s
    </pre>
    </div>
    </td>
    <td class="text-center" style="vertical-align: middle"><div id='div_%(tid)s_screenshot' class="collapse in">%(screenshot)s</div></td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    # 失败 的样式，去掉原来JS效果，美化展示效果  -Findyou / 美化类名上下居中，无截图列 -- Gelomen
    REPORT_TEST_WITH_OUTPUT_TMPL_0 = r"""
    <tr id='%(tid)s' class='%(Class)s'>
        <td class='%(style)s' style="vertical-align: middle"><div class='testcase'>%(name)s</div></td>
        <td style="vertical-align: middle">%(doc)s</td>
        <td colspan='5' align='center'>
        <!--默认收起错误信息 -Findyou
        <button id='btn_%(tid)s' type="button"  class="btn btn-xs collapsed" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
        <div id='div_%(tid)s' class="collapse">  -->

        <!-- 默认展开错误信息 -Findyou /  修复失败按钮的颜色 -- Gelomen -->
        <button id='btn_%(tid)s' type="button"  class="btn btn-xs" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
        <div id='div_%(tid)s' class="collapse in">
        <pre style="text-align:left">
        %(script)s
        </pre>
        </div>
        </td>
        <td class='%(style)s' style="vertical-align: middle"></td>
    </tr>
    """  # variables: (tid, Class, style, desc, status)

    # 通过 的样式，加标签效果  -Findyou / 美化类名上下居中 -- Gelomen
    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s' style="vertical-align: middle"><div class='testcase'>%(name)s</div></td>
    <td style="vertical-align: left">%(doc)s</td>
    <td colspan='5' align='center'><span class="label label-success success">%(status)s</span></td>
    <td class='%(style)s' style="vertical-align: middle"></td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #
    # 增加返回顶部按钮  --Findyou
    ENDING_TMPL = """<div id='ending'>&nbsp;</div>
    <div id="toTop" style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer; display: none">
    <a><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>
    """


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        # 增加一个测试通过率 --Findyou
        self.passrate = float(0)

        # 增加失败用例合集
        self.failCase = ""
        # 增加错误用例合集
        self.errorCase = ""

    def startTest(self, test):
        stream = sys.stderr
        # stdout_content = " Testing: " + str(test)
        # stream.write(stdout_content)
        # stream.flush()
        # stream.write("\n")
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector
        self.test_start_time = round(time.time(), 2)

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        self.test_end_time = round(time.time(), 2)
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        use_time = round(self.test_end_time - self.test_start_time, 2)
        self.result.append((0, test, output, '', use_time))
        if self.verbosity > 1:
            sys.stderr.write('  S  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('  S  ')
            sys.stderr.write('\n')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        use_time = round(self.test_end_time - self.test_start_time, 2)
        self.result.append((2, test, output, _exc_str, use_time))
        if self.verbosity > 1:
            sys.stderr.write('  E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('  E  ')
            sys.stderr.write('\n')

        # 添加收集错误用例名字 -- Gelomen
        self.errorCase += "<li>" + str(test) + "</li>"

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        use_time = round(self.test_end_time - self.test_start_time, 2)
        self.result.append((1, test, output, _exc_str, use_time))
        if self.verbosity > 1:
            sys.stderr.write('  F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('  F  ')
            sys.stderr.write('\n')

        # 添加收集失败用例名字 -- Gelomen
        self.failCase += "<li>" + str(test) + "</li>"


class HTMLTestRunner(Template_mixin):
    """
    """

    def __init__(self, stream=sys.stdout, verbosity=2, title=None, description=None, tester=None, build=None):
        self.need_screenshot = 0
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
        if tester is None:
            self.tester = self.DEFAULT_TESTER
        else:
            self.tester = tester
        if build is None:
            self.build = self.DEFAULT_BUILD
        else:
            self.build = build
        self.startTime = datetime.datetime.now()

    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity)  # verbosity为1,只输出成功与否，为2会输出用例名称
        test(result)
        self.stopTime = datetime.datetime.now()
        self.generateReport(test, result)
        # 优化测试结束后打印蓝色提示文字 -- Gelomen
        print("\n\033[36;0m--------------------- Test Finished ---------------------\n"
              "------------- Total time: %s -------------\033[0m" % (self.stopTime - self.startTime), file=sys.stderr)
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e, s in result_list:
            cls = t.__class__
            if cls not in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e, s))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    # 替换测试结果status为通过率 --Findyou
    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        status.append('Total %s' % (result.success_count + result.failure_count + result.error_count))
        if result.success_count:
            status.append('pass %s' % result.success_count)
        if result.failure_count:
            status.append('Fail %s' % result.failure_count)
        if result.error_count:
            status.append('Error %s' % result.error_count)
        if status:
            status = '，'.join(status)
            if (result.success_count + result.failure_count + result.error_count) > 0:
                self.passrate = str("%.2f%%" % (float(result.success_count) / float(
                    result.success_count + result.failure_count + result.error_count) * 100))
            else:
                self.passrate = "0.00 %"
        else:
            status = 'none'

        if len(result.failCase) > 0:
            failCase = result.failCase
        else:
            failCase = "Not Exist"

        if len(result.errorCase) > 0:
            errorCase = result.errorCase
        else:
            errorCase = "Not Exist"

        return [
            ('Tester', self.tester),
            ('Start Time', startTime),
            ('Duration', duration.split(".")[0]),
            ('Status', status + "，Pass rate = " + self.passrate),
            ('Fail Case', failCase),
            ('Error Case', errorCase),
            ('Build', self.build),
        ]

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s'
        stylesheet = self._generate_stylesheet()
        # 添加 通过、失败 和 错误 的统计，以用于饼图  -- Gelomen
        passed = self._generate_report(result)["Pass"]
        fail = self._generate_report(result)["fail"]
        error = self._generate_report(result)["error"]

        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)["report"]
        ending = self._generate_ending()
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            Pass=passed,
            fail=fail,
            error=error,
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(output.encode('utf8'))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    # 增加Tester显示 -Findyou
    # 增加 失败用例合集 和 错误用例合集 的显示  -- Gelomen
    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            # 如果是 失败用例 或 错误用例合集，则不进行转义 -- Gelomen
            if name == "Fail Case":
                if value == "Not Exist":
                    line = self.HEADING_ATTRIBUTE_TMPL % dict(
                        name=name,
                        value="<ol style='float: left;'>" + value + "</ol>",
                    )
                else:
                    line = self.HEADING_ATTRIBUTE_TMPL % dict(
                        name=name,
                        value="<div class='panel-default' style='float: left;'><a class='showDetail' data-toggle='collapse' href='#failCaseOl' style='text-decoration: none;'>Open</a></div>"
                              "<ol id='failCaseOl' class='collapse' style='float: left;'>" + value + "</ol>",
                    )
            elif name == "Error Case":
                if value == "Not Exist":
                    line = self.HEADING_ATTRIBUTE_TMPL % dict(
                        name=name,
                        value="<ol style='float: left;'>" + value + "</ol>",
                    )
                else:
                    line = self.HEADING_ATTRIBUTE_TMPL % dict(
                        name=name,
                        value="<div class='panel-default' style='float: left;'><a class='showDetail' data-toggle='collapse' href='#errorCaseOl' style='text-decoration: none;'>Open</a></div>"
                              "<ol id='errorCaseOl' class='collapse' style='float: left;'>" + value + "</ol>",
                    )
            else:
                line = self.HEADING_ATTRIBUTE_TMPL % dict(
                    name=saxutils.escape(name),
                    value=saxutils.escape(value),
                )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
            tester=saxutils.escape(self.tester),
            Build=saxutils.escape(self.build),
        )
        return heading

    # 生成报告  --Findyou添加注释
    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        # 所有用例统计耗时初始化
        sum_ns = 0
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = ns = 0
            for n, t, o, e, s in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                elif n == 2:
                    ne += 1
                ns += s  # 把单个class用例文件里面的多个def用例每次的耗时相加
            ns = round(ns, 2)
            sum_ns += ns  # 把所有用例的每次耗时相加
            # format class description
            # if cls.__module__ == "__main__":
            #     name = cls.__name__
            # else:
            #     name = "%s.%s" % (cls.__module__, cls.__name__)
            name = cls.__name__
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            # desc = doc and '%s - %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                name=name,
                doc=doc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
                time_usage=str(ns) + "sec"  # 单个用例耗时
            )
            rows.append(row)

            for tid, (n, t, o, e, s) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)
        sum_ns = round(sum_ns, 2)
        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            time_usage=str(sum_ns) + "sec",  # 所有用例耗时
            passrate=self.passrate,
        )

        # 获取 通过、失败 和 错误 的统计并return，以用于饼图  -- Gelomen
        Pass = str(result.success_count)
        fail = str(result.failure_count)
        error = str(result.error_count)
        return {"report": report, "Pass": Pass, "fail": fail, "error": error}

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1_1', 'ft1_1', 'et1_1'etc
        has_output = bool(o or e)
        # ID修改点为下划线,支持Bootstrap折叠展开特效 - Findyou
        if n == 0:
            tid_flag = 'p'
        elif n == 1:
            tid_flag = 'f'
        elif n == 2:
            tid_flag = 'e'
        tid = tid_flag + 't%s_%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        # desc = doc and ('%s - %s' % (name, doc)) or name

        # utf-8 支持中文 - Findyou
        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            # uo = o.decode('latin-1')
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            # ue = e.decode('latin-1')
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )

        # 截图名字通过抛出异常存放在u，通过截取字段获得截图名字  -- Gelomen
        u = uo + ue
        # 先判断是否需要截图
        self.need_screenshot = u.find("screenshotImg[")

        if self.need_screenshot == -1:
            tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL_0 or self.REPORT_TEST_NO_OUTPUT_TMPL

            row = tmpl % dict(
                tid=tid,
                Class=(n == 0 and 'hiddenRow' or 'none'),
                style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'passCase'),
                name=name,
                doc=doc,
                script=script,
                status=self.STATUS[n],
            )
        else:
            tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL_1 or self.REPORT_TEST_NO_OUTPUT_TMPL

            screenshot_list = re.findall("screenshotImg\[(.*?)\]screenshotImg", u)
            screenshot = ""
            for i in screenshot_list:
                screenshot += "</br><img src=\"image/" + i + "\" width= 90 height=180></br><a class=\"screenshot\" href=\"javascript:void(0)\" img=\"image/" + i + "\">" + i + "</a>"

            # screenshot = u[u.find('screenshotImg[') + 9:u.find(']screenshotImg')]
            # browser = u[u.find('browser[') + 8:u.find(']browser')]

            row = tmpl % dict(
                tid=tid,
                Class=(n == 0 and 'hiddenRow' or 'none'),
                style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'passCase'),
                name=name,
                doc=doc,
                script=script,
                status=self.STATUS[n],
                screenshot=screenshot,
            )
        rows.append(row)

        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL

class DirAndFiles(object):

    def __init__(self):
        self.path = "report/"
        self.title = "Test Report"

    # Local용 레포트 저장 패스 생성 처리
    def create_dir(self, title=None):
        i = 1.0

        if title is not None:
            self.title = title

        dir_path = self.path + self.title + "V" + str(round(i, 1))

        while True:
            is_dir = os.path.isdir(dir_path)
            if is_dir:
                i += 0.1
                dir_path = self.path + self.title + "V" + str(round(i, 1))
            else:
                break

        os.makedirs(dir_path)
        report_path = dir_path + "/" + self.title + "V" + str(round(i, 1)) + ".html"
        GlobalMsg.set_value("dir_path", dir_path)
        GlobalMsg.set_value("report_path", report_path)

    @staticmethod
    def set_jenkins_dir(run_info):
        if run_info == "stickerAndroid":
            DirAndFiles.dir_path = "/Users/st20073c/lfk_jenkins/workspace/LFK_Yuki_Automation_Test_sticker_Android/report/"
        elif run_info == "stickerIos":
            DirAndFiles.dir_path = "/Users/st20073c/lfk_jenkins/workspace/LFK_Yuki_Automation_Test_sticker_iOS/report/"
        elif run_info == "cmsMonitoring":
            DirAndFiles.dir_path = "/Users/st20073c/lfk_jenkins/workspace/LFK_Yuki_Automation_CMS_Monitoring/report/"
        DirAndFiles.report_path = "report/index.html"
        GlobalMsg.set_value("dir_path", DirAndFiles.dir_path)
        GlobalMsg.set_value("report_path", DirAndFiles.report_path)

    @staticmethod
    def get_screenshot(driver):
        i = 1

        # 전역 변수를 통해 폴더 경로 얻기
        new_dir = GlobalMsg.get_value("dir_path")
        img_dir = new_dir + "/image"

        # 폴더의 존재 여부를 판단하고 존재하지 않으면 작성
        is_dir = os.path.isdir(img_dir)
        if not is_dir:
            os.makedirs(img_dir)

        img_path = img_dir + "/" + str(i) + ".png"

        # 동일한 테스트 절차가 잘못되어 캡처 이름처럼 파일을 덮어쓰게 될 수 있으므로 이름이 존재하면 id가 추가됨
        while True:
            is_file = os.path.isfile(img_path)
            if is_file:
                i += 1
                img_path = img_dir + "/" + str(i) + ".png"
            else:
                break
        driver.get_screenshot_as_file(img_path)
        img_name = str(i) + ".png"

        print("screenshotImg[" + img_name + "]screenshotImg")

    @staticmethod
    def get_logcat(driver):

        now = datetime.datetime.now()
        now_time = '%s-%s-%s' % (now.year, now.month, now.day)

        # Log path 지정(없으면 생성)
        new_dir = GlobalMsg.get_value("dir_path")
        log_path = new_dir + "/log"
        is_dir = os.path.isdir(log_path)
        if not is_dir:
            os.makedirs(log_path)

        # Log 취득
        logs = driver.get_log('logcat')
        log_messages = list(map(lambda log: log['message'], logs))

        # Log 이름 설정 > Log path 에 text 파일 생성
        log_name = "Log_by_automation_script_"+now_time+".txt"
        filepath = os.path.join(log_path, log_name)

        # txt파일에 Log 출력
        log = open(filepath, "w")
        for i in range(1, 11):
            log.write('\n'.join(log_messages))
        log.close()

        print("logText[" + log_name + "]logText")

##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
