from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep
import os
#导入动作链对应的类
from selenium.webdriver import ActionChains
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, 'chromedriver.exe')
bro = webdriver.Chrome(service=Service(image_path))
#需求：模拟登录QQ空间 3ZUnM2IY
bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
a_tag = bro.find_element('id','switcher_plogin')
a_tag.click()
sleep(1)
#输入账号和密码
userName_tag = bro.find_element('id','u')
password_tag = bro.find_element('id','p')
sleep(1)
userName_tag.send_keys('2971470335')
sleep(1)
password_tag.send_keys('3ZUnM2IY')
sleep(1)
#点击登录按钮
btn = bro.find_element('id','login_button')
btn.click()
sleep(3)

#滑块验证码的处理
#1.判断是否有滑块验证码的存在
#2.如果有滑块验证码的存在则进行滑块验证码的处理
#3.如果没有滑块验证码的存在则进行下一步的操作
#判断是否有滑块验证码的存在
try:
    bro.switch_to.frame('tcaptcha_iframe_dy')
    sleep(1)
    #获取滑块标签
    div_tag = bro.find_element('xpath','//*[@id="tcOperation"]/div[6]')
    #动作链
    action = ActionChains(bro)
    #点击长按指定的标签
    action.click_and_hold(div_tag)
    for i in range(5):
        #perform()立即执行动作链操作
        #move_by_offset(x,y) x水平方向 y竖直方向
        action.move_by_offset(30,0).perform()
        sleep(0.3)
    #释放动作链
    action.release()
    sleep(1)
except:
    print('没有滑块验证码')
    pass