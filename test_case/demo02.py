from pages.welcome_page import WelcomePage
from common_tools.app_driver import driver
from common_tools.assert_ui import assertui
import allure


@allure.epic("��Ŀ����������Ŀ���ƣ��������д�õ����ĸ�app�汾�����Ե�")
@allure.feature("ģ�飺������ĸ�ģ�飬����APP�ĵ�¼ҳ")
class TestWelcome:

    # @allure.title("��֤����׿app��װж��")
    # @allure.description("Ԥ�ڣ�������װж��")
    # @allure.testcase("https://pms.reolink.com.cn/index.php?m=testcase&f=view&caseID=54170&version=0")
    # def test_install_apk(self):
    #     """
    #     ���򳡾�
    #     �Զ���������ţ�1001
    #     �������ƣ���֤��װж��app
    #     """
    #     driver.init_driver()  # �����ֻ�
    #     driver.uninstall_app()  # ���app������ж��app
    #     driver.install_app()  # ��װapp

    @allure.title("��֤��������д�Զ�����������")
    @allure.description("Ԥ�ڣ���дԤ�ڽ��")
    @allure.testcase("������д�����϶�Ӧ��ĳ���Զ����������ӵ�ַ")
    def test_disagree_terms(self):
        driver.start_app()
        welcome = WelcomePage()  # ��ʼ����ӭҳ��ҳ�����
        welcome.click_disagree_exit_btn()  # �������ͬ�Ⲣ�˳�����ť
        driver.stop_app()  # ֹͣapp
        driver.clear_app_cache()  # ���app����

    @allure.title("��֤��ͬ��")
    @allure.description("Ԥ�ڣ�ͬ��")
    @allure.testcase("ͬ��")
    def test_agree_terms(self):
        driver.start_app()
        welcome = WelcomePage()  # ��ʼ����ӭҳ��ҳ�����
        welcome.click_terms_conditions_icon()  # �����ѡ�������������ѡ��
        assertui.assert_clickable('com.mcu.reolink:id/btn', True)  # ���Ե����ѡ���ͬ�Ⲣ��������ť�Ŀɵ��״̬
        welcome.click_agree_continue_btn()  # �����ͬ�Ⲣ��������ť
        driver.stop_app()  # ֹͣapp
        driver.clear_app_cache()  # ���app����
