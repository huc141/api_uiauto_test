import pytest
from common_tools.app_driver import driver
from pages.rn_device_setting_page.remote_setting import RemoteSetting
from common_tools.read_yaml import read_yaml
from common_tools.assert_ui import assertui


class TestRemoteSettingAudio:
    def test_remote_setting_audio(self):
        # ����app��������¼��
        driver.start_app(True)

        # ���豸�б���ҵ���Ӧ�豸������Զ������
        RemoteSetting().scroll_click_remote_setting(device_name="Reolink TrackMix WiFi")

        # ��ȡ��ǰҳ�����й����д��txt�ļ��У�ͳ�Ƴ���������

        # ��ȡԤ�ڹ�������������ȡ���Ĺ��������һһ�ȶԺ������˶�

        # ����

