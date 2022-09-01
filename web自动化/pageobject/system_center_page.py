import time
import datetime
import allure

from base.base_page import BasePage
from selenium.webdriver.common.by import By
class Systemcenter(BasePage):
    username=(By.XPATH,"//input[@id='account']")
    password=(By.XPATH,"//input[@id='password']")
    login=(By.XPATH,"//button[@type='submit']")
    wo=(By.XPATH,"//*[text()='我知道了']")
    systemmange=(By.XPATH,"/html/body/div[1]/div/div[1]/div[3]/div[2]/div[2]")
    fabuzhidu=(By.LINK_TEXT,"发布制度")
    zhidubiaoti=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.title']/span/input")
    zhidubianhao=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.code']/span/input")
    zhiduguisuzhuzhi=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.belongToBu']/span/span[1]/span[1]/span/input")
    organizationname=(By.XPATH,"/html/body/div[5]/div/ul/li/div/span")
    virtualgroup=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.scopePartitionList']/span/span[1]/span[1]/span/input")
    virtual=(By.XPATH,"/html/body/div[6]/div/ul/li/div/span")
    corepeople=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.coreUserGroup']/span/span[1]/span[1]/span/input")
    aliyun=(By.XPATH,"//span[text()='阿x集x(Corp)']")
    systemclassification=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.categorySecondId']/span/span[1]/span[2]/span/i")
    classification=(By.XPATH,"//*[@id='153']/div/div/div")
    system_level=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.levelSecond']/span/span[1]/span[2]/span[1]/i")
    management_system=(By.XPATH,"//span[text()='管理制度']")
    liaisons=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.ownerUserId']/span/span[1]/span[1]/span/input")
    system_liaisons=(By.XPATH,"/html/body/div[8]/div/ul/li/div/span/div")
    date_format_input_box=(By.XPATH,"//input[@placeholder='请选择日期']")
    input_date=(By.XPATH,"/html/body/div[9]/div/div[1]/span/input")
    employee_interests=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.hasInterestRelation']/div[2]/label[1]")
    intern_visible=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.isWbVisible']/div[2]/label[1]")
    apply_for_download=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.isDownload']/div[2]/label[2]")
    regulatory_compliance=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.isInvolvedCompliance']/div[2]/label[1]")
    offline_approval=(By.XPATH,"//*[@id='baseInfo.NO_NAME_FIELD_$0.NO_NAME_FIELD_$1.isOfflineApproved']/div[2]/label[2]")
    next_step=(By.XPATH,"//*[@id='whale-page']/div[2]/div/button[2]/span")
    input_box=(By.XPATH,"/html/body")
    next_step1=(By.XPATH,"//*[@id='whale-page']/div[2]/div/button[2]/span")
    shangchuan=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.attachments']/div[2]/div/div/button/span")
    ifeame=(By.XPATH,"//iframe[@class='e_iframe whale-editor-iframe']")
    clear_text1=(By.XPATH,"/html/body")
    add_text=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.faqs']/div[2]/div[2]/button")
    FAQ_issue=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.faqs.0.question']/span/textarea")
    FAQ_answer=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.faqs.0.answer']/span/textarea")
    flow=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.flows']/div[2]/div[2]/button")
    flow_name=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.flows.0.flowName']/span/input")
    flow_classify=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.flows.0.flowType']/span/span[1]/span[1]/span/input")
    on_line=(By.XPATH,"/html/body/div[5]/div/ul/li[1]")
    flow_explain=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.flows.0.flowLink']/span/input")
    add_upstream=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.relation.NO_NAME_FIELD_$1.parentRelations']/div[2]/div[2]/button")
    upstream=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.relation.NO_NAME_FIELD_$1.parentRelations.0.relationId']/span/span[1]/span[1]/span/input")
    one_text=(By.XPATH,"/html/body/div[5]/div/ul/li[1]")
    add_downstream=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.relation.NO_NAME_FIELD_$1.childRelations']/div[2]/div[2]/button")
    downstream=(By.XPATH,"//*[@id='NO_NAME_FIELD_$0.relation.NO_NAME_FIELD_$1.childRelations.0.relationId']/span/span[1]/span[1]/span/input")
    one_text1=(By.XPATH,"/html/body/div[6]/div/ul/li[1]")
    submit=(By.XPATH,"//*[@id='whale-page']/div[2]/div/button[5]")
    def system_login(self,name,pawd):
        time.sleep(5)
        with allure.step('step1:进入统一登录中心'):
            self.send_keys(self.username,name)
        with allure.step('step2:输入账号密码'):
            self.send_keys(self.password,pawd)
            self.max_windows()
        with allure.step('step3:登录成功'):
            self.click(self.login)
            time.sleep(5)
        try:
            assert self.find_element(self.wo).text == "我知道了"
            self.logging.info("断言成功，成功登录制度中心")
        except Exception as e:
            self.logging.error("断言失败，登录制度中心失败")
            self.save_screenshot()
            raise e

    def release_system(self,name,pawd,biaoti,bianhao,organization,group,people,liaison,today_date,ceshi,file_path1,issue,answer,flow_name_1,explain,upstream_text,downstream_text):
        with allure.step('step1:进入统一登录中心'):
            time.sleep(2)
            self.send_keys(self.username, name)
        with allure.step('step2:输入账号密码'):
            self.send_keys(self.password, pawd)
        with allure.step('step3:登录成功'):
            self.max_windows()
            self.click(self.login)
            time.sleep(8)
        with allure.step('step1:点击-我知道了'):
            self.click(self.wo)
        with allure.step('step2:点击-制度管理'):
            self.click(self.systemmange)
        with allure.step('step3:点击发布制度'):
            self.click(self.fabuzhidu)
            time.sleep(3)
        with allure.step('step4:输入制度标题'):
            self.send_keys(self.zhidubiaoti,biaoti)
        with allure.step('step5:输入制度编号'):
            self.send_keys(self.zhidubianhao,bianhao)
        with allure.step('step6:选择制度归属组织'):
            self.send_keys(self.zhiduguisuzhuzhi,organization)
            time.sleep(3)
        with allure.step('step7:点击阿x巴x'):
            self.click(self.organizationname)
        with allure.step('step8:选择虚拟分组'):
            self.send_keys(self.virtualgroup,group)
            time.sleep(3)
        with allure.step('step9:点击虚拟分组'):
            self.click(self.virtual)
        with allure.step('step10:选择核心人群'):
            self.send_keys(self.corepeople,people)
            time.sleep(3)
        with allure.step('step11:点击阿里云客服'):
            self.click(self.aliyun)
        with allure.step('step12:选择制度分类'):
            self.click(self.systemclassification)
            time.sleep(3)
        with allure.step('step13:点击分类test'):
            self.click(self.classification)
        with allure.step('step14:点击制度级别下拉框'):
            self.click(self.system_level)
        with allure.step('step15:点击管理制度'):
            self.click(self.management_system)
        with allure.step('step16:输入制度联络人'):
            self.send_keys(self.liaisons,liaison)
            time.sleep(4)
        with allure.step('step17:点击丁承勇'):
            self.click(self.system_liaisons)
        with allure.step('step18:点击日期选择框'):
            self.click(self.date_format_input_box)
        with allure.step('step19:输入当天日期'):
            self.send_keys(self.input_date,today_date)
            # self.click(self.next_step)
            time.sleep(3)
        with allure.step('step20:点击是否涉及员工利益选择是'):
            self.click(self.employee_interests)
        with allure.step('step21:外包实习生是否可见选择是'):
            self.click(self.intern_visible)
        with allure.step('step22:是否申请下载下载否'):
            self.click(self.apply_for_download)
        with allure.step('step23:是否涉及监管合规选择是'):
            self.click(self.regulatory_compliance)
        with allure.step('step24:是否已经线下审批选择否'):
            self.click(self.offline_approval)
        with allure.step('step25:点击下一步'):
            self.click(self.next_step)
            time.sleep(5)
        with allure.step('step26:再一次点击下一步'):
            self.click(self.next_step)
            time.sleep(3)
            self.switch_to_frame(self.ifeame)
            # self.clear_text(self.clear_text1)
        with allure.step('step27:富文本框输入内容'):
            self.click_enter(self.input_box,ceshi)
            self.quit_frame()
            time.sleep(3)
        with allure.step('step28:点击下一步'):
            self.click(self.next_step1)
            time.sleep(5)
        with allure.step('step29:点击上传附件'):
            self.update_file(self.shangchuan,file_path1)
            time.sleep(5)
        with allure.step('step30:点击下一步'):
            self.click(self.next_step)
        with allure.step('step31:点击新增FAQ内容'):
            time.sleep(3)
            self.click(self.add_text)
        with allure.step('step32:输入问题'):
            self.send_keys(self.FAQ_issue,issue)
        with allure.step('step33:输入FAQ回答'):
            self.send_keys(self.FAQ_answer,answer)
        with allure.step('step34:点击下一步'):
            self.click(self.next_step)
        with allure.step('step35:点击相关流程-新增内容'):
            time.sleep(3)
            self.click(self.flow)
        with allure.step('step36:输入流程名称'):
            self.send_keys(self.flow_name,flow_name_1)
        with allure.step('step37:点击流程父类'):
            self.click(self.flow_classify)
        with allure.step('step38:选择线上'):
            self.click(self.on_line)
        with allure.step('step39:输入流程说明'):
            self.send_keys(self.flow_explain,explain)
        with allure.step('step40:点击下一步'):
            self.click(self.next_step)
        with allure.step('step41:添加上游制度'):
            time.sleep(3)
            self.click(self.add_upstream)
        with allure.step('step42:输入上游制度内容'):
            self.send_keys(self.upstream,upstream_text)
        with allure.step('step43：选择第一个内容'):
            self.click(self.one_text)
        with allure.step('step44:添加下游制度'):
            self.click(self.add_downstream)
        with allure.step('step45:输入下游制度内容'):
            self.send_keys(self.downstream,downstream_text)
        with allure.step('step46:选择阿林'):
            self.click(self.one_text1)
        with allure.step('step47:点击提交'):
            self.click(self.submit)
            time.sleep(3)
            self.alert_accept()

