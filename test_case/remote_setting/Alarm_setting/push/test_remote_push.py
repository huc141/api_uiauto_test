# -*- coding: utf-8 -*-
import pytest
import allure
from common_tools.app_driver import driver
from common_tools.read_yaml import read_yaml
from pages.base_page import BasePage
from pages.rn_device_setting_page.remote_push_notifications import RemotePush
from pages.rn_device_setting_page.remote_setting import RemoteSetting

devices_config = read_yaml.load_device_config(yaml_file_name='push.yaml')  # 读取参数化文件


@allure.epic("远程配置>报警通知>手机推送")
class TestRemotePush:

    @pytest.mark.parametrize("device_config", devices_config)
    @allure.feature("推送主页>主页文案")
    @allure.story("需人工核查日志和录屏")
    @allure.title('测试推送主页文案')
    @pytest.mark.skip
    def test_remote_push_main_text(self, device_config):
        # 检查键是否存在，存在则执行当前用例，否则跳过
        remote_items = device_config['ipc']['push']['items']
        BasePage().check_key_in_yaml(remote_items, 'push')

        # 启动app，并开启录屏
        driver.start_app(True)

        # 设备列表中滚动查找到单机、nvr、hub并进入远程配置，在远程设置主页点击菜单项@allure.feature
        RemoteSetting().access_in_push_notifications(device_list_name=device_config['device_list_name'])

        # 验证push主页文案列表
        key_res = BasePage().is_key_in_yaml(remote_items['push'], 'supported_test')
        RemotePush().check_push_main_text(main_text=remote_items['push_text'],
                                          options=remote_items['push']['options'],
                                          supported_test=key_res,
                                          other_switch=remote_items)

    @pytest.mark.parametrize("device_config", devices_config)
    @allure.feature("访客电话提醒")
    @allure.story("需人工核查日志和录屏")
    @allure.title('测试访客电话提醒')
    @pytest.mark.skip
    def test_remote_non_detection_area(self, device_config):
        # 检查键是否存在，存在则执行当前用例，否则跳过
        remote_items = device_config['ipc']['push']['items']
        BasePage().check_key_in_yaml(remote_items, 'visitor_phone_remind')

        # 启动app，并开启录屏
        driver.start_app(True)

        # 设备列表中滚动查找到单机、nvr、hub并进入远程配置，在远程设置主页点击菜单项@allure.feature
        RemoteSetting().access_in_push_notifications(device_list_name=device_config['device_list_name'])

        # 开启访客电话提醒并验证【访客电话提醒】在主页的文案
        RemotePush().turn_on_visitor_phone_remind()

    @pytest.mark.parametrize("device_config", devices_config)
    @allure.feature("设备通知铃声")
    @allure.story("需人工核查日志和录屏")
    @allure.title('测试设备通知铃声')
    @pytest.mark.skip
    def test_device_notify_ringtone(self, device_config):
        # 检查键是否存在，存在则执行当前用例，否则跳过
        remote_items = device_config['ipc']['push']['items']
        BasePage().check_key_in_yaml(remote_items, 'device_notify_ringtone')

        # 启动app，并开启录屏
        driver.start_app(True)

        # 设备列表中滚动查找到单机、nvr、hub并进入远程配置，在远程设置主页点击菜单项@allure.feature
        RemoteSetting().access_in_push_notifications(device_list_name=device_config['device_list_name'])

        # 开启设备通知铃声并验证【设备通知铃声】在主页的文案
        RemotePush().turn_on_device_notify_ringtone()

        # 遍历报警铃声
        RemotePush().verify_device_notify_ringtone(text=remote_items['device_notify_ringtone']['alarm_ring']['text'],
                                                   options=remote_items['device_notify_ringtone']['alarm_ring'][
                                                       'options'])

    @pytest.mark.parametrize("device_config", devices_config)
    @allure.feature("计划")
    @allure.story("需人工核查日志和录屏")
    @allure.title('测试【计划】')
    @pytest.mark.skip
    def test_remote_push_plan(self, device_config):
        # 检查键是否存在，存在则执行当前用例，否则跳过
        remote_items = device_config['ipc']['push']['items']
        BasePage().check_key_in_yaml(remote_items, 'schedule')

        # 启动app，并开启录屏
        driver.start_app(True)

        # 设备列表中滚动查找到单机、nvr、hub并进入远程配置，在远程设置主页点击菜单项@allure.feature
        RemoteSetting().access_in_push_notifications(device_list_name=device_config['device_list_name'])

        # 验证 计划主页的文案，验证报警类型
        key_res = BasePage().is_key_in_yaml(remote_items['schedule'], 'alarm_type')
        RemotePush().verify_push_plan(texts_list=remote_items['schedule']['text'],
                                      supported_alarm_type=key_res,
                                      options_text=remote_items['schedule']['alarm_type'])  # 计划主页的文案

    @pytest.mark.parametrize("device_config", devices_config)
    @allure.feature("推送间隔")
    @allure.story("需人工核查日志和录屏")
    @allure.title('测试推送间隔')
    @pytest.mark.skip
    def test_push_interval(self, device_config):
        # 检查键是否存在，存在则执行当前用例，否则跳过
        remote_items1 = device_config['ipc']['push']['items']
        BasePage().check_key_in_yaml(remote_items1, 'schedule')

        remote_items = device_config['ipc']['push']['items']['schedule']
        BasePage().check_key_in_yaml(remote_items, 'push_interval')

        # 启动app，并开启录屏
        driver.start_app(True)

        # 设备列表中滚动查找到单机、nvr、hub并进入远程配置，在远程设置主页点击菜单项@allure.feature
        RemoteSetting().access_in_push_notifications(device_list_name=device_config['device_list_name'])

        # 测试推送间隔和文案
        RemotePush().verify_test_push_interval(texts_list=remote_items['push_interval']['text'],
                                               option_text_list=remote_items['push_interval']['option'])

    @pytest.mark.parametrize("device_config", devices_config)
    @allure.feature("延时通知")
    @allure.story("需人工核查日志和录屏")
    @allure.title('测试延时通知')
    @pytest.mark.skip
    def test_push_delay_notifications(self, device_config):
        # 检查键是否存在，存在则执行当前用例，否则跳过
        remote_items = device_config['ipc']['push']['items']
        BasePage().check_key_in_yaml(remote_items, 'delay_notifications')

        # 启动app，并开启录屏
        driver.start_app(True)

        # 设备列表中滚动查找到单机、nvr、hub并进入远程配置，在远程设置主页点击菜单项@allure.feature
        RemoteSetting().access_in_push_notifications(device_list_name=device_config['device_list_name'])

        # 遍历延迟时间
        RemotePush().verify_delay_notifications(text=remote_items['delay_notifications']['delay_time']['text'],
                                                options=remote_items['delay_notifications']['delay_time']['option_text'])

