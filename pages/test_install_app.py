from pages.welcome_page import WelcomePage
from common_tools.app_driver import driver
from common_tools.assert_ui import assertui
import allure


@allure.epic("��Ŀ��Android-Reolink-P2PCN-4.45.0.3.20240508")
@allure.feature("ģ�飺APP��װ")
class TestInstallApp:

    @allure.title("��֤����׿app��װ")
    @allure.description("Ԥ�ڣ�������װ")
    @allure.testcase("https://pms.reolink.com.cn/index.php?m=testcase&f=view&caseID=54170&version=0")
    def test_install_apk(self):
        """
        ���򳡾�
        �Զ���������ţ�1001
        �������ƣ���֤��װapp
        """
        driver.init_driver()  # �����ֻ�
        driver.uninstall_app()  # ���app������ж��app
        driver.install_app()  # ��װapp
