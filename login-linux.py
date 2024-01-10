import socket
import os
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# try:
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
# except ImportError:
#     os.system('pip install -i https://pypi.mirrors.ustc.edu.cn/simple/ selenium')
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By

# your account and password
account = 'A0xxxxxxx'
password = '1234xxxxxx'
# /path/to/your/chromedriver/
chrome_path = '/home/epicr/user/AHU-AutoLogin/chromedriver/chromedriver'
service = Service(chrome_path)

# 获取本地DHCP服务器分配的内网ip
ipaddr = socket.gethostbyname(socket.gethostname())
# 拼接成登陆地址ip
url = 'http://172.16.253.3/a79.htm?wlanuserip=' + ipaddr + '&wlanacname=&wlanacip=172.16.253.1'

# 浏览器后台运行
option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument('--disable-gpu')
browser = webdriver.Chrome(service=service, options=option)
browser.get(url)

browser.minimize_window()

# 获取输入框和登陆按钮
inputaccount = browser.find_element(By.XPATH, value='//form[@name="f1"]/input[@name="DDDDD"]')
inputpassword = browser.find_element(By.XPATH, value='//form[@name="f1"]/input[@name="upass"]')
submitbutton = browser.find_element(By.XPATH, value='//form[@name="f1"]/input[@name="0MKKey"]')

# 模拟登陆
inputaccount.send_keys(account)
inputpassword.send_keys(password)
# time.sleep(5)
submitbutton.submit()

browser.quit()
