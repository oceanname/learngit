import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# value=driver.find_element(By.XPATH,"//span[text()='按图片搜索']").get_attribute('class')
# print(value)
from pageobject.login_page import LoginPage
from comm.logging import Log
log=Log()


@allure.issue('https://aone.alibaba-inc.com/project/949683/issue',name='aone地址')
@allure.testcase('https://julita.alibaba-inc.com/#/use-case',name='聚例塔')
@allure.epic('淘宝的web自动化')
class Test_taobao:
    @allure.feature('淘宝登录')
    @allure.story('登录淘宝')
    @allure.title('正确登录淘宝')
    def test_login(self):
        with allure.step('step1：打开登录页'):
             lg = LoginPage()
        with allure.step('step2:登录账号密码'):
             lg.login_taobao('17305803265', 'op3819941016op1')
        with allure.step('step3:淘宝登录成功'):
             pass
        log.info('登录淘宝成功')
