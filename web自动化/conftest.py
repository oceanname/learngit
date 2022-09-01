import time
import os
from py._xmlgen import html
import allure
import pytest
from selenium import webdriver

driver = None
from comm.logging import Log
# @pytest.fixture(scope="function",autouse=True)
# def open():
#     lg = LoginPage()
#     lg.login_taobao('17305803265','op3819941016op1')

#通过conftest来实现报告的描述
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))  #html报告中插入一列，列头名为Description

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    try:
        cells.insert(1, html.td(report.description))
    except:
        pass
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅获取用例call且执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图..'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

@pytest.fixture(scope='session')
def browser():
    global driver
    if driver is None:
        driver =webdriver.Chrome()
    yield driver
    print("关闭浏览器")
    driver.quit()
