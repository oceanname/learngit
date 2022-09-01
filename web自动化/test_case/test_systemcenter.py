import datetime
import time
import pytest
import allure
from comm.logging import Log
from comm.yaml import Yamlutil
from pageobject.system_center_page import Systemcenter
from base.base_page import BasePage
log=Log()
now_time=str(datetime.datetime.now())
today=datetime.datetime.today()
today_date=str(datetime.datetime.strftime(today,'%Y-%m-%d'))
date_time=str(datetime.datetime.strftime(today,'%Y-%m-%d %H:%M:%S'))
@allure.issue('https://aone.alibaba-inc.com/project/949683/issue',name='aone地址')
@allure.testcase('https://julita.alibaba-inc.com/#/use-case',name='聚例塔')
@allure.epic('制度中心的web自动化')
@pytest.mark.flaky(reruns=0, reruns_delay=2)
class Test_system:

    @allure.feature('登录制度中心')
    @allure.title('正确登录制度中心')
    def test_login_center(self):
        Sy=Systemcenter()
        Sy.system_login('dcy01378776','op94857op')
    @allure.feature('发布制度流程')
    @allure.title('发布制度')
    @pytest.mark.parametrize('caseinfo',Yamlutil().read_case_yaml('process.yaml'))
    def test_release_system(self,caseinfo):
        Systemcenter().release_system(caseinfo['name'],caseinfo['pawd'],caseinfo['biaoti']+date_time,caseinfo['bianhao']+date_time,caseinfo['organization'],caseinfo['group'],caseinfo['people'],caseinfo['liaison'],today_date,caseinfo['ceshi'],caseinfo['file_path'],caseinfo['issue'],caseinfo['answer'],caseinfo['flow_name'],caseinfo['explain'],caseinfo['upstream_text'],caseinfo['downstream_text'])

