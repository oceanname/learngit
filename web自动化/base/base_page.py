
import logging
import time
import traceback
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import allure
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from comm.logging import Log
url='https://www.taobao.com/'
url1='https://regulation.alibaba.net/'

class BasePage:

    def __init__(self):
        self.logging=Log()
    # def open_brower(self):
        global driver
        self.driver = webdriver.Chrome()
        driver=self.driver
    # def get(self,url):
        self.driver.get(url1)
    #定位元素
    def find_element(self,args):
        try:
            self.logging.info('定位元素{0}成功'.format(args))
            return self.driver.find_element(*args)
        except Exception as e:
            self.logging.error('定位元素{0}失败'.format(e))
            self.save_screenshot()
            raise
    #等待元素可见
    def wait_element_to_be_visible(self,loc,timeout=10,frequency=0.5):
        '''
               等待元素可见
               :param loc: 元素定位的XPATH元组表达式
               :param timeout: 等待的超时时间
               :param frequency: 轮询频率
               :return:
               '''
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            self.logging.info("等待元素{0}可见".format(loc))
        except Exception as e:
            self.logging.error("等待元素{0}可见失败".format(loc))
            self.save_screenshot()
            raise e
    #等待元素存在
    def wait_element_to_be_exist(self,loc,timeout=10,frequency=0.5):
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_element_located(loc))
            self.logging.info("等待元素{0}存在".format(loc))
        except Exception as e:
            self.logging.error("页面元素{0}等待存在失败".format(loc))
            raise e
    #清除文本内容
    def clear_text(self,args,timeout=10,frequency=0.5):
       try:
           self.click(args,timeout,frequency)
           self.find_element(args).clear()
           self.logging.info("清除元素{0}的文本内容成功".format(args))
       except Exception as e:
           self.logging.error("清除元素{0}的文本内容失败".format(args))
           raise e
    #输入
    def send_keys(self,args,value,timeout=10,frequency=0.5):
        try:
            self.logging.info('在元素{0}中输入内容：{1}'.format(args,value))
            self.wait_element_to_be_visible(args,timeout,frequency)
            self.find_element(args).send_keys(value)
        except Exception as e:
            self.logging.error('查找不到{0}元素，无法输入{1}'.format(args,value))
            raise e
    #点击
    def click(self,args,timeout=10,frequency=0.5):
        try:
            self.wait_element_to_be_visible(args,timeout,frequency)
            self.find_element(args).click()
            self.logging.info('找到元素{0}进行点击'.format(args))
        except Exception as e:
            self.logging.error('查找不到{0}，无法点击'.format(args))
            raise e
    #进入框架
    def swith_to_frame(self,frame_name):
        try:
            self.driver.switch_to.frame(frame_name)
            self.logging.info('进入框架{0}成功'.format(frame_name))
        except Exception as e:
            self.logging.error('进入框架失败：{0}'.format(e))
            raise

    def switch_to_frame(self, loc, timeout=20, frequency=0.5):
        '''
        切换iframe页面
        :param loc: 元素定位的XPATH元组表达式
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            self.logging.info("根据元素<{}>进行iframe切换".format(loc))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.frame_to_be_available_and_switch_to_it(loc))
        except Exception as e:
            self.logging.error("根据元素<{}>进行iframe切换失败！".format(loc))
            raise e
        else:
            end_time = time.time()
            self.logging.info("根据元素<{}>进行iframe切换，等待时间：{}秒".format(loc, round(end_time - start_time, 2)))
    #出框架
    def quit_frame(self):
        try:
            self.logging.info('退出框架成功')
            self.driver.switch_to.default_content()
        except Exception as e:
            self.logging.error('退出框架失败：{0}'.format(e))
            raise
    #选择下拉框
    def choise_select(self,args,value):
        try:
            self.logging.info('定位{0}成功，选择{1}'.format(args,value))
            sel=Select(self.find_element(args))
            sel.select_by_value(value)
        except Exception as e:
            self.logging.error('定位下拉框{0}失败'.format(args))
            raise e
    #获取对象的文本值
    def get_element_text(self, loc,timeout=20, frequency=0.5):
        try:
            self.logging.info("获取元素{0}的文本值".format(loc))
            self.wait_element_to_be_visible(loc,timeout,frequency)
            return self.find_element(loc).text
        except Exception as e:
            self.logging.error("获取元素{0}的文本值失败".format(loc))
            raise e
    #获取对象属性值
    def get_element_attr(self, attr_name, loc, timeout=20, frequency=0.5):
        try:
            self.logging.info("获取对象{0}的属性值".format(loc))
            self.wait_element_to_be_exist(loc,timeout,frequency)
            return self.find_element(loc).get_attribute(attr_name)
        except Exception as e:
            self.logging.error("获取元素属性{0}的属性{1}的值失败".format(loc,attr_name))
            raise e
    # 获取与切换窗口句柄
    def switch_to_window_handles(self):

        try:
            self.logging.info('更换窗口成功')
            # 获取当前窗口句柄
            now_handle = self.driver.current_window_handle
            # 获取所有窗口句柄
            all_handles = self.driver.window_handles
            # 循环遍历所有新打开的窗口句柄
            for handle in all_handles:
                if handle != now_handle:
                    # 切换窗口
                    self.driver.switch_to.window(handle)

        except Exception as e:
            self.logging.error('切换窗口失败')
            print(traceback.format_exc())
            raise e
    #全屏浏览器
    def max_windows(self):
        try:
            self.logging.info('浏览器放大至全屏')
            self.driver.maximize_window()
        except Exception as e:
            self.logging.error('浏览器放大全屏失败{0}'.format(e))
            raise
    #alert弹窗
    def alert_accept(self):
        try:
            self.driver.switch_to.alert.accept()
            self.logging.info('确定alert弹窗')
        except Exception as e:
            self.logging.error('确定alert弹窗失败{0}'.format(e))
            raise
    #输入alert弹窗内容
    def alert_send(self,loc):
        try:
            self.driver.switch_to.alert.send_keys(loc)
            self.alert_accept()
            self.logging.info('输入{0}alert弹窗成功'.format(loc))
        except Exception as e:
            self.logging.error('输入alert弹窗失败{0}'.format(e))
            raise
    #弹窗关闭
    def alert_close(self, alert_type='alert', text=None, timeout=20, frequency=0.5):
        '''
        :param alert_type: 弹框类型：alert/confirm/prompt
        :param text: prompt弹框输入的文本
        :param timeout: 等待的超时时间
        :param frequency: 轮询频率
        :return:
        '''
        try:
            self.logging.info("在切换并关闭{}类型的弹框".format(alert_type))
            start_time = time.time()
            WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present())
            if alert_type in ['alert', 'confirm']:
                self.driver.switch_to.alert.accept()
            elif alert_type == 'prompt':
                self.driver.switch_to.alert.send_keys(text)
                self.driver.switch_to.alert.accept()
            else:
                self.logging.error("不支持{},请确认alert的类型".format(alert_type))
        except Exception as e:
            self.logging.error("在切换并关闭{}类型的弹框失败！".format(alert_type))
            raise e
        else:
            end_time = time.time()
            self.logging.info("在切换并关闭{}类型的弹框，等待时间：{}秒".format(alert_type, round(end_time - start_time, 2)))
    #文件上传
    # def update(self,args):
    #     try:
    #         self.click(args)
    #         app = pywinauto.Desktop()  # 使用pywinauto来选择文件
    #         dlg = app["打开"]  # 选择文件上传的窗口
    #         dlg["Toolbar3"].click()  # 选择文件地址输入框
    #         send_keys("D:\图片")  # 键盘输入上传文件的路径
    #         send_keys("{VK_RETURN}")  # 键盘输入回车，打开该路径
    #         dlg["文件名(&N):Edit"].type_keys("鼠.jpg")  # 选中文件名输入框，输入文件名
    #         dlg["打开(&O)"].click()  # 点击打开
    #         self.logging.info('打开文件图片')
    #     except Exception as e:
    #         self.logging.error('打开文件图片失败{0}'.format(e))
    def update_file(self,args,file_path):
        self.click(args)
        time.sleep(2)
        nol=win32gui.FindWindow("#32770","打开")                          #一级窗口
        combo_box_ex32=win32gui.FindWindowEx(nol,0,"ComboBoxEx32",None)  #二级窗口；父级，0表示第一个，自己类名，文本内容，没有未None
        combo_box=win32gui.FindWindowEx(combo_box_ex32,0,"ComboBox",None)#三级窗口；
        edit=win32gui.FindWindowEx(combo_box,0,"Edit",None)              #四级窗口
        button=win32gui.FindWindowEx(nol,0,"Button","打开(&O)")           #二级打开按钮
        time.sleep(3)
        win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)    #输入文件地址
        time.sleep(3)
        win32gui.SendMessage(nol,win32con.WM_COMMAND,1,button)           #点击打开按钮，提交文件

    # def upload_file(self, filename, browser_type="chrome"):
    #     '''
    #     非input标签的文件上传
    #     :param filename: 文件名（绝对路径）
    #     :param browser_type: 浏览器类型
    #     :return:
    #     '''
    #     try:
    #         self.logging.info("上传文件（{}）".format(filename))
    #         time.sleep(2)
    #         upload(filePath=filename, browser_type=browser_type)
    #     except Exception as e:
    #         self.logging.error("上传文件（{}）失败！".format(filename))
    #         raise e
    #     else:
    #         time.sleep(2)
    #鼠标悬浮
    def suspend_mouse(self, loc, timeout=20, frequency=0.5):
        try:
            self.logging.info("在元素{0}上进行悬浮".format(loc))
            self.click(loc,timeout,frequency)
            ele=self.find_element(loc)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            self.logging.error("在元素{0}上进行悬浮失败".format(loc))
            raise e

    def save_screenshot(self):
        '''
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        '''
        file_name = "./image" + "\\{}.png".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(body=file,name=file_name,attachment_type=allure.attachment_type.PNG)
        self.logging.info("页面截图文件保存在：{}".format(file_name))
    #模拟输入后回车操作
    def click_enter(self,args,value,timeout=10,frequency=0.5):
        try:
            self.logging.info('在元素{0}中输入内容：{1}后进行回车'.format(args,value))
            self.wait_element_to_be_visible(args,timeout,frequency)
            self.find_element(args).send_keys(value,Keys.ENTER)
        except Exception as e:
            self.logging.error('查找不到{0}元素，无法输入{1}进行回车'.format(args,value))
            raise e