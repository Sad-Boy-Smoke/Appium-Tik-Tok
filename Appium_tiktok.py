import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from keyboard import is_pressed
from selenium.webdriver.common.keys import Keys
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.zhiliaoapp.musically',
    appActivity='com.ss.android.ugc.aweme.splash.SplashActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'

driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

def check_click_element(path): #функция для проверки наличия элемента
    while True:
        try:
            el = driver.find_element(by=AppiumBy.XPATH, value=path)
            el.click()
            print('удача')

        except NoSuchElementException:
            
            if is_pressed('enter'):
                break
            print('не удача')
            continue
        break
def go_swipe():
    sleep(0.5)
    print('я уебище не свайпнул опять')
    driver.swipe(100, 2000, 100, 100, duration=150)
    sleep(0.5)
def write_in_list_tag():

    with open('C:/Bot_tt/Tag_list.txt', 'r') as file:
        lines = [line for line in file]
        print('33333333333333333333333333333333333333333333333333333333333333333333333333333333')
        return lines  
def upper_video(number):
    print('11111111111111111111111111111111111111111111111111111111111111111111111111111111')
    print(number)
    # a = '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zhiliaoapp.musically:id/dbr"]/android.widget.FrameLayout[' + str(number)  + str(']')
    # print(a)
    # b = (str("'")+a+str("'"))
    # print(b)
    check_click_element('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.zhiliaoapp.musically:id/dbr"]/android.widget.FrameLayout[3]')
    check_click_element('//android.widget.LinearLayout[@resource-id="com.zhiliaoapp.musically:id/g4e"]')
    print("222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")



def go_push_tag():
    
    read_lines = write_in_list_tag()
    while True:    
        try:
            share_tag = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.zhiliaoapp.musically:id/z3"]')
            share_tag.click()
            break
        except:
            print('Не могу найти поле тэгов, я ебач')
            continue
    
    while True:
        try:
            push_tag = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.zhiliaoapp.musically:id/c_f"]')
            break
        except:
            continue
            
    for i in read_lines:
        push_tag.send_keys(str(i))
    
    
    
    
def log(): # по задумке служит для первичной настройки tik tok
    print('Нажать закрыть предложение гугла ебаного')
    check_click_element('//android.widget.ImageView[@content-desc="Cancel"]')
    print('Нажать вход через гугл')
    check_click_element('(//android.view.ViewGroup[@resource-id="com.zhiliaoapp.musically:id/be1"])[3]')
    print('')
    check_click_element('(//android.widget.LinearLayout[@resource-id="com.google.android.gms:id/container"])[1]')
    print('')
    check_click_element('(//android.widget.LinearLayout[@resource-id="com.zhiliaoapp.musically:id/e1x"])[1]')
    print('')
    check_click_element('//android.widget.Button[@resource-id="com.zhiliaoapp.musically:id/c04"]')
    print('')
    check_click_element('//android.widget.TextView[@resource-id="com.zhiliaoapp.musically:id/j41"]')
    print('')
    check_click_element('//android.widget.Button[@text="Later"]')
    print('')
    check_click_element('//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')

    sleep(3)
    go_swipe()
    
    print('Нажать на выложить видео')
    check_click_element('//android.widget.Button[@content-desc="Create"]/android.widget.ImageView')
    
    print('Нажать на не давать разрешение на запись видео')
    check_click_element('//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
    
    print('Нажать на не разрешать микрофон')
    check_click_element('//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
    
    print('Нажать на выбрать видео')
    check_click_element('(//android.widget.FrameLayout[@resource-id="com.zhiliaoapp.musically:id/fpp"])[1]')
    
    print('Нажать allow all для всех файлов')
    check_click_element('//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_allow_all_button"]')
log() 
while True:
    video_number_input = input('Введите номер видео: ')
    if video_number_input.strip() == "":
        print("Вы не ввели номер видео.")
        continue
    else:
        upper_video(int(video_number_input))
        break
go_push_tag()
check_click_element('dfwew')
driver.quit()
