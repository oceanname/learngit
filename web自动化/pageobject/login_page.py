import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    login=(By.LINK_TEXT,'登录')
    username=(By.XPATH,"//input[@id='fm-login-id']")
    password=(By.XPATH,"//input[@id='fm-login-password']")
    denglu=(By.XPATH,"//button[@type='submit']")
    def login_taobao(self,name,paword):
        # self.open_brower()
        # self.get('https://www.taobao.com/')
        self.click(self.login)
        time.sleep(3)
        self.switch_to_window_handles()
        time.sleep(3)
        self.max_windows()
        self.send_keys(self.username,name)
        self.send_keys(self.password,paword)
        self.click(self.denglu)