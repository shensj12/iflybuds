from selenium.webdriver.common.by import By

# guidepageView
# 用户服务协议和隐私政策确认页
Link_service = (By.LINK_TEXT, '《用户服务协议》')
Link_privacy = (By.LINK_TEXT, '《隐私政策》')
Btn_back = (By.ID, 'tws.iflytek.headset:id/back')
Btn_confim = (By.ID, 'tws.iflytek.headset:id/privacy_confirm')
Btn_disagree = (By.ID, 'tws.iflytek.headset:id/privacy_exit')
Web_view = (By.ID, 'tws.iflytek.headset:id/web_view')
# 点击不同意后的确认提示框
User_tip = (By.ID, 'tws.iflytek.headset:id/tv_usertip')
Btn_exit = (By.ID, 'tws.iflytek.headset:id/cancel')
Btn_confim2 = (By.ID, 'tws.iflytek.headset:id/comfirm')
# 获取权限知晓页
per_layout = (By.ID, 'tws.iflytek.headset:id/user_permission_list_layout')
Btn_confim3 = (By.ID, 'tws.iflytek.headset:id/permission_confirm')
Btn_skip = (By.ID, 'tws.iflytek.headset:id/permission_cancel')
# 手机页面中iflybuds图标
iflbuds = (By.XPATH, '//android.widget.TextView[@content-desc="iFLYBUDS"]')
# 登录页标题
btn_title = (By.ID, 'tws.iflytek.headset:id/authsdk_title_view')

# loginView

# 固件升级取消
update_cancle = (By.ID, 'tws.iflytek.headset:id/firmware_update_cancel')
# 关闭广告
close_ad = (By.ID, 'tws.iflytek.headset:id/close')
phonenum_type = (By.ID, 'tws.iflytek.headset:id/input')
btn_getver = (By.ID, 'tws.iflytek.headset:id/button_tv')
wechat_btn = (By.ID, 'tws.iflytek.headset:id/login_type_wx')
btn_set = (By.XPATH,
           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
           '.widget.RelativeLayout/android.widget.LinearLayout['
           '2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c['
           '4]/android.widget.FrameLayout')
btn_setting_account = (By.ID, 'tws.iflytek.headset:id/setting_account')
btn_loginout = (By.ID, 'tws.iflytek.headset:id/login_out')
btn_authsdk_login = (By.ID, 'tws.iflytek.headset:id/authsdk_login_view')
# 首次登录授权按钮
btn_location_allow = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
btn_file_allow = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
# 引导页按钮
btn_next = (By.ID, 'tws.iflytek.headset:id/next')
# 授权请求-允许访问手机信息
btn_access = (By.ID, 'tws.iflytek.headset:id/permission_phone_layout')
btn_device_allow = (By.ID, 'com.android.permissioncontroller:id/permission_allow_button')
wechat_double_first = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget'
                                 '.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager'
                                 '/android.widget.GridView/android.widget.LinearLayout['
                                 '1]/android.widget.LinearLayout/android.widget.ImageView')
# mainpageView
close_first_record_prompt = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                       '.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout'
                                       '/android.widget.LinearLayout[2]/android.widget.ImageView')
Btn_iknow = (By.ID, 'tws.iflytek.headset:id/confirm')
scan_url = (By.ID, 'tws.iflytek.headset:id/url')
Btn_scan = (By.ID, 'tws.iflytek.headset:id/right_img')
Left_config = (By.ID, 'tws.iflytek.headset:id/left_config')
Right_config = (By.ID, 'tws.iflytek.headset:id/right_config')
Voice_config = (By.ID, 'tws.iflytek.headset:id/voice_layout')
Btn_IFLYBUDS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout['
                          '2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c['
                          '1]/android.widget.FrameLayout/android.widget.ImageView')

Sel_start_stop = (By.ID, 'tws.iflytek.headset:id/lf_start_stop_lay')
Sel_nextsong = (By.ID, 'tws.iflytek.headset:id/lf_next_lay')
Sel_presong = (By.ID, 'tws.iflytek.headset:id/lf_pre_lay')
# Sel_voicedial=(By.ID,'tws.iflytek.headset:id/lf_wake_lay') 白
Sel_System_assistant = (By.ID, 'tws.iflytek.headset:id/lf_start_stop_call_record_lay')
Sel_pat_close = (By.ID, 'tws.iflytek.headset:id/lf_close_lay')
Sel_hang_up = (By.ID, 'tws.iflytek.headset:id/lf_hang_up_lay')
Sel_start_record = (By.ID, 'tws.iflytek.headset:id/lf_start_record_lay')
Sel_phone_close = (By.ID, 'tws.iflytek.headset:id/lf_dial_close_lay')

choose_nextsong = (By.ID, 'tws.iflytek.headset:id/lf_next')
choose_start_record = (By.ID, 'tws.iflytek.headset:id/lf_start_record')
choose_presong = (By.ID, 'tws.iflytek.headset:id/lf_pre')
choose_hang_up = (By.ID, 'tws.iflytek.headset:id/lf_hang_up')

Btn_hx = (By.ID, 'tws.iflytek.headset:id/voice_layout')
Sel_hxvoicedial = (By.ID, 'tws.iflytek.headset:id/app_layout')
Sel_VoiceAssistant = (By.ID, 'tws.iflytek.headset:id/sys_lay')
Sel_hx_close = (By.ID, 'tws.iflytek.headset:id/close_lay')


Btn_start_record = (By.ID, 'tws.iflytek.headset:id/start_btn')
Btn_stop_record = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                             '2]/android.widget.LinearLayout[2]/android.widget.ImageView')
Sel_audiorecord = (By.XPATH,
                   '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                   '.FrameLayout[2]/android.widget.LinearLayout')
Sel_Microphonerecord = (By.XPATH,
                        '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                        '.FrameLayout[3]/android.widget.LinearLayout')
Sel_dialrecord = (By.XPATH,
                  '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget'
                  '.FrameLayout[1]/android.widget.LinearLayout')
Sel_first_trial = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.LinearLayout')
Sel_tryout = (By.ID, 'tws.iflytek.headset:id/positive')
Sel_notrial = (By.ID, 'tws.iflytek.headset:id/cancel')
Btn_float = (By.ID, 'tws.iflytek.headset:id/float_state')
Allow_float = (By.ID, 'tws.iflytek.headset:id/permission_layout')
Config_get = (By.ID, 'android:id/switch_widget')
Config_back = (By.XPATH, '//android.widget.ImageButton[@content-desc="向上导航"]')

Btn_change_language = (By.ID, 'tws.iflytek.headset:id/language_layout')
# 外语
Btn_language_other = (By.ID, 'tws.iflytek.headset:id/language_grid_tab_other')
Btn_english = 'new UiSelector().textContains("英语")'
# 中文
Btn_language_chinese = (By.ID, 'tws.iflytek.headset:id/language_grid_tab_cn')
Btn_putonghua = (By.XPATH,
                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout'
                 '/android.widget.LinearLayout['
                 '2]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout['
                 '1]/android.widget.TextView')

Btn_sichuanhua = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                            '.LinearLayout/android.widget.LinearLayout['
                            '2]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout[2]')

check_sichuanhua = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView'
                                     '/android.widget.LinearLayout/android.widget.LinearLayout['
                                     '4]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                     '4]/android.widget.LinearLayout/android.widget.ImageView')
Btn_simultaneous = (By.ID, 'tws.iflytek.headset:id/msc_check')
Btn_pop_close = (By.ID, 'tws.iflytek.headset:id/pop_close')
# 结束录音
Btn_end_record = (By.ID, 'tws.iflytek.headset:id/hangup_btn')

# 录音时转文字
Btn_transtext = (By.ID, 'tws.iflytek.headset:id/call_record_asr_layout')
# 录音记录内转文字
Btn_record_transtext = (By.ID, 'tws.iflytek.headset:id/start_rec_layout')
trans_putonghua = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.LinearLayout/android.widget.LinearLayout['
                             '2]/android.widget.LinearLayout/android.widget.GridView/android.widget.LinearLayout['
                             '1]/android.widget.TextView')
# recordingView
play_audio = (By.ID, 'tws.iflytek.headset:id/play_audio_layout')
no_search_result = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                              '.LinearLayout/android.widget.TextView')
delete_search = (By.ID, 'tws.iflytek.headset:id/delete_search')
Btn_search_icon = (By.ID,'tws.iflytek.headset:id/left_img')
Btn_search_confirm = (By.ID, 'tws.iflytek.headset:id/cancel')
Btn_search_result = (By.ID, 'tws.iflytek.headset:id/container')
Btn_search = (By.ID, 'tws.iflytek.headset:id/search_edit')
Btn_confirm = (By.ID, 'tws.iflytek.headset:id/pop_confirm')
Btn_cloud_backup=(By.ID,"tws.iflytek.headset:id/auto_upload")
not_wifi_hint = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.LinearLayout/android.widget.LinearLayout')
Btn_cloud = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                       '/android.widget.RelativeLayout/android.widget.LinearLayout['
                       '2]/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout'
                       '/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.LinearLayout/android'
                       '.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget'
                       '.RelativeLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                       '.LinearLayout/android.widget.LinearLayout['
                       '3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ImageView')
Btn_recording_menu = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android'
                                '.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c[2]/android'
                                '.widget.FrameLayout/android.widget.ImageView')
Img_records = (By.ID, 'tws.iflytek.headset:id/title_txt')
first_record = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout['
                             '2]/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget'
                             '.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget'
                             '.LinearLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView'
                             '/android.widget.RelativeLayout['
                             '1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
record_pause = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout['
                          '2]/android.widget.LinearLayout/android.widget.FrameLayout')
record_title = (By.ID, 'tws.iflytek.headset:id/title_record')
Btn_more = (By.ID, 'tws.iflytek.headset:id/right_image')
Btn_share = (By.ID, 'tws.iflytek.headset:id/share')
delete_record = (By.ID, 'tws.iflytek.headset:id/delete_layout')
delete_record_confirm = (By.ID, 'tws.iflytek.headset:id/pop_confirm')
Btn_share_url = (By.ID, 'tws.iflytek.headset:id/share_url_txt')
Btn_share_text = (By.ID, 'tws.iflytek.headset:id/share_txt_txt')
Btn_share_out = (By.ID, 'tws.iflytek.headset:id/share_out_txt')
Btn_share_email = (By.ID, 'tws.iflytek.headset:id/share_email_txt')
Btn_cancel = (By.ID, 'tws.iflytek.headset:id/pop_cancel')
Check_share_url = (By.ID, 'tws.iflytek.headset:id/share_wx')
Check_share_text = (By.ID, 'tws.iflytek.headset:id/share_wx')
Check_share_out = (By.ID, 'tws.iflytek.headset:id/share_txt')
Check_share_audio = (By.ID, 'tws.iflytek.headset:id/share_audio')
Check_share_email = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                               '.Button')
More_dict_row = {Btn_share_url: Check_share_url, Btn_share_text: Check_share_text, Btn_share_out: Check_share_out,
             Btn_share_email: Check_share_email}
# 区分
more_col_01 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout['
                         '1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
# 原始记录
more_col_02 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout['
                         '2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
# 上传云端
more_col_03 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout['
                         '3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
# 翻译
more_col_04 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout['
                         '4]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
# 复制
more_col_05 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout['
                         '5]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
# 摘要
more_col_06 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout[1]/android.widget.ListView/android.widget.LinearLayout['
                         '6]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout')
name_bar = (By.ID, 'tws.iflytek.headset:id/caller_name')

wechat_forward_first = (By.XPATH, '//android.widget.FrameLayout[@content-desc="当前所在页面,'
                                  '选择"]/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                  '/android.widget.FrameLayout['
                                  '1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget'
                                  '.RelativeLayout['
                                  '2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                                  '.LinearLayout')
wechat_forward_confirm = (By.ID, 'com.tencent.mm:id/ffp')
back_iflybuds = (By.ID, 'com.tencent.mm:id/ffb')
abst_share_url = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                            '.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout['
                            '1]/android.widget.LinearLayout')
abst_share_text = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout['
                             '2]/android.widget.LinearLayout')
abst_output = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout['
                         '4]/android.widget.LinearLayout')
keep_cloud_delete = (By.ID, 'tws.iflytek.headset:id/checkbox')
upload_icon = (By.ID, 'tws.iflytek.headset:id/upload_icon')
# download_record = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
#                              '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
#                              '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout['
#                              '2]/android.widget.LinearLayout/android.widget.FrameLayout')
refresh_icon = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout['
                          '1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout'
                          '/android.widget.ImageView')
# settingView
float_view_check = (By.ID, 'tws.iflytek.headset:id/float_view_check')
float_view_check_question = (By.ID, 'tws.iflytek.headset:id/qa')
float_view_check_iknow = (By.ID, 'tws.iflytek.headset:id/i_know')

Btn_voice_wakeup = (By.ID, 'tws.iflytek.headset:id/setting_wakeword_tv')
xiaofei_wakeup = (By.ID, 'tws.iflytek.headset:id/app_layout')
check_xiaofei = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget'
                           '.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView')
Btn_dial = (By.ID, 'tws.iflytek.headset:id/setting_call_helper')
Btn_contact_alias = (By.ID, 'tws.iflytek.headset:id/contact_alias')
check_contact_alias = (By.ID, 'tws.iflytek.headset:id/videoview')
Btn_setting_menu = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android'
                              '.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c[4]/android.widget'
                              '.FrameLayout/android.widget.ImageView')
Title_text = (By.ID, 'tws.iflytek.headset:id/title_txt')
setting_left_config = (By.ID, 'tws.iflytek.headset:id/setting_tws_config_left')
setting_right_config = (By.ID, 'tws.iflytek.headset:id/setting_tws_config_right')
prev_song = (By.ID, 'tws.iflytek.headset:id/lf_pre_lay')
Btn_help_back = (By.ID, 'tws.iflytek.headset:id/ysf_title_bar_back_area')
Btn_setting_call_record = (By.ID, 'tws.iflytek.headset:id/setting_call_record')
Btn_english_check = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget'
                               '.LinearLayout/android.widget.LinearLayout['
                               '4]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                               '2]/android.widget.LinearLayout/android.widget.ImageView')
Btn_telephone = (By.ID, 'tws.iflytek.headset:id/setting_account')
Btn_nickname = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.ImageView')
nick_name = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                       '/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')
Btn_save = (By.ID, 'tws.iflytek.headset:id/save')
Btn_webpage = (By.ID, 'tws.iflytek.headset:id/web_layout')
Btn_process = (By.ID, 'tws.iflytek.headset:id/process_keep_alive')
Btn_instructions = (By.ID, 'tws.iflytek.headset:id/setting_use_help')
Btn_FQAs = (By.ID, 'tws.iflytek.headset:id/setting_fqa')
Btn_help = (By.ID, 'tws.iflytek.headset:id/setting_feedback')
Btn_us = (By.ID, 'tws.iflytek.headset:id/setting_about_us')
Btn_privacy = (By.ID, 'tws.iflytek.headset:id/privacy_layour')
check_privacy = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget'
                           '.LinearLayout/android.widget.LinearLayout')
Setting_putonghua = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget'
                               '.LinearLayout/android.widget.LinearLayout['
                               '4]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                               '1]/android.widget.LinearLayout')
Check_setting_putonghua = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView'
                                     '/android.widget.LinearLayout/android.widget.LinearLayout['
                                     '4]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout['
                                     '1]/android.widget.LinearLayout/android.widget.ImageView')
check_content_telephone = (By.ID, 'tws.iflytek.headset:id/login_out')
check_content_process = (By.ID, 'tws.iflytek.headset:id/device_choose')
check_content_instructions = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                        '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                        '.LinearLayout['
                                        '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit'
                                        '.WebView/android.view.View/android.view.View[1]/android.view.View[1]')
check_content_FQAs = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                                '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView'
                                '/android.view.View/android.view.View[2]')
check_content_help = (By.ID, 'tws.iflytek.headset:id/send_message_button')
check_content_us = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.ImageView')
close_webpage = (By.ID, 'tws.iflytek.headset:id/close')
setting_dict = {Btn_telephone: check_content_telephone, Btn_webpage: close_webpage,
                Btn_process: check_content_process, Btn_dial: check_contact_alias,
                Btn_instructions: check_content_instructions, Btn_FQAs: check_content_FQAs,
                Btn_help: check_content_help, Btn_us: check_content_us, Btn_privacy: check_privacy}

Sub_btn_image = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                           '.view.View/android.view.View[1]/android.view.View[1]')
Sub_btn_video = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                           '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                           '.view.View/android.view.View[1]/android.view.View[2]')
Sub_image_01 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[1]')
Sub_image_02 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[2]')
Sub_image_03 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[3]')
Sub_image_04 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[4]')
Sub_image_05 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[5]')
Sub_image_06 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[6]')
Sub_image_07 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                          '.view.View/android.view.View[2]/android.view.View[7]')
image_list = [Sub_image_01, Sub_image_02, Sub_image_03, Sub_image_04, Sub_image_05, Sub_image_06, Sub_image_07]
check_sub_image = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                             '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                             '.view.View/android.view.View[1]')
fqa_01 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.LinearLayout['
                    '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                    '.View/android.view.View[1]/android.view.View[2]/android.view.View[2]')
fqa_02 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.LinearLayout['
                    '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                    '.View/android.view.View[1]/android.view.View[2]/android.view.View[5]')
fqa_03 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.LinearLayout['
                    '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                    '.View/android.view.View[1]/android.view.View[4]/android.view.View[2]')
fqa_04 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.LinearLayout['
                    '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                    '.View/android.view.View[1]/android.view.View[4]/android.view.View[5]')
fqa_05 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.LinearLayout['
                    '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                    '.View/android.view.View[1]/android.view.View[4]/android.view.View[8]')
fqa_06 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                    '/android.widget.LinearLayout/android.widget.LinearLayout['
                    '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                    '.View/android.view.View[1]/android.view.View[6]/android.view.View[2]')
fqa_check = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                       '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                       '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                       '.View/android.view.View[1]')
fqa_list = [fqa_01, fqa_02, fqa_03, fqa_04, fqa_05, fqa_06]
app_search_oneplus = (By.ID, 'net.oneplus.launcher:id/search_all_apps')
app_icon_oneplus = (By.ID, 'net.oneplus.launcher:id/icon')
Sub_video_01 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[3]')
Sub_video_02 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[4]')
Sub_video_03 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[5]')
Sub_video_04 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[6]')
Sub_video_05 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[7]')
Sub_video_06 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[9]')
Sub_video_07 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[10]')
Sub_video_08 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[11]')
Sub_video_09 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[12]')
Sub_video_10 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[13]')
Sub_video_11 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[8]')
Sub_video_12 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[9]')
Sub_video_13 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[10]')
Sub_video_14 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[12]')
Sub_video_15 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                          '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                          '.View/android.view.View[13]')


video_list_white = [Sub_video_01, Sub_video_02, Sub_video_03, Sub_video_04, Sub_video_05, Sub_video_06, Sub_video_07,
              Sub_video_08, Sub_video_09, Sub_video_10, Sub_video_11, Sub_video_12, Sub_video_13, Sub_video_14,
              Sub_video_15]

video_list_black = [Sub_video_01, Sub_video_02, Sub_video_04, Sub_video_05, Sub_video_11, Sub_video_06, Sub_video_07,
              Sub_video_08]

check_sub_video = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                             '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android'
                             '.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View['
                             '2]/android.widget.Button')
Btn_refresh = (By.ID, 'tws.iflytek.headset:id/refresh')
Btn_scan_page = (By.ID, 'tws.iflytek.headset:id/zxing')
Btn_weibo = (By.ID, 'tws.iflytek.headset:id/about_us_visit_wb')
Btn_official = (By.ID, 'tws.iflytek.headset:id/about_us_visit_official')
Btn_firmware = (By.ID, 'tws.iflytek.headset:id/setting_firmware_update')
Btn_firmware_back = (By.ID, 'tws.iflytek.headset:id/firmware_update_back')
check_firmware = (By.ID, 'tws.iflytek.headset:id/firmware_done_sn_layout')
check_weibo = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                         '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                         '.View/android.view.View[1]/android.view.View[4]/android.view.View[1]')
check_official = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout['
                         '2]/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view'
                         '.View/android.view.View[1]')


# finderView
Btn_contact_access = (By.ID, 'tws.iflytek.headset:id/layout_contacts')
Btn_finder_menu = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout['
                             '2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/b.b.k.a.c['
                             '3]/android.widget.FrameLayout/android.widget.ImageView')
Btn_relax = (By.ID, 'tws.iflytek.headset:id/discover_music_type_img')
Btn_like = (By.ID, 'tws.iflytek.headset:id/faved')
Btn_clock = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                       '/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout'
                       '/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget'
                       '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                       '.LinearLayout[2]/android.widget.ImageView')
time_bar = (By.ID, 'tws.iflytek.headset:id/timerseekbar')
close_time = (By.ID, 'tws.iflytek.headset:id/dialog_close')
Btn_voice_dial = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                            '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout['
                            '2]/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget'
                            '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout['
                            '1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout')
Start_voice_dial = (By.ID, 'tws.iflytek.headset:id/next_btn')
Btn_start_use = (By.ID, 'tws.iflytek.headset:id/btn_complete')
Img_wakeup_style = (By.ID, 'tws.iflytek.headset:id/imv_wakeupstyle')
Btn_dial_back = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                           '.RelativeLayout/android.widget.LinearLayout[1]/android.widget.ImageView')
relax_title = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                         '.RelativeLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android'
                         '.widget.TextView')

finder_pause_music = (By.ID, 'tws.iflytek.headset:id/discover_music_state_img')
close_music_bar = (By.ID, 'tws.iflytek.headset:id/discover_music_state_close')

# 腾讯会议
Desktop_wemeet = (By.XPATH, '//android.widget.TextView[@content-desc="腾讯会议"]')
Btn_fast_meeting = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                              '.ViewGroup/android.view.ViewGroup[1]/android.widget.LinearLayout['
                              '2]/android.widget.LinearLayout[2]')
Btn_enter_meeting = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view'
                               '.ViewGroup/android.view.ViewGroup[4]')
Btn_close_meeting = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.RelativeLayout/android.view.ViewGroup[1]/android.widget.TextView')
Btn_close_meeting_plus = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android'
                                    '.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                                    '.RelativeLayout[3]')
Btn_restore_cancel = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                '.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget'
                                '.TextView[1]')
Title_tengxun = (By.ID, 'tws.iflytek.headset:id/tc_layout')
Title_confirm = (By.ID, 'tws.iflytek.headset:id/comfirm')
Having_meeting_end = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                       '/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[2]')
# 喜马拉雅FM
Desktop_ximalaya = (By.XPATH, '//android.widget.TextView[@content-desc="喜马拉雅"]')
Btn_ranking = (By.XPATH, '//android.widget.Button[@content-desc="排行榜"]/android.widget.ImageView')
Ranking_first = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget'
                           '.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget'
                           '.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android'
                           '.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.ListView/android.widget.LinearLayout['
                           '1]/android.widget.RelativeLayout')
all_play = (By.ID, 'com.ximalaya.ting.android:id/main_tv_play_control')
play_bar = (By.ID, 'com.ximalaya.ting.android:id/main_fragment_playbar')
Btn_pause = (By.ID, 'com.ximalaya.ting.android:id/main_iv_play_btn_center_icon')
Btn_YiHouZaiShou = (By.ID, 'com.ximalaya.ting.android:id/main_negative_button')

# 更新
close_upgrade = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget'
                           '.LinearLayout[2]/android.widget.ImageView')




