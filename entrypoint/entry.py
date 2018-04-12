# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import os
import time

width = os.getenv("BROWSER_WIDTH", None)
height = os.getenv("BROWSER_HEIGHT", None)
team_id = os.getenv("TEAMSPIRIT_ID", None)
user_id = os.getenv("TEAMSPIRIT_USER_ID", None)
user_pass = os.getenv("TEAMSPIRIT_USER_PASSWORD", None)

login_url = "https://{}.cloudforce.com/".format(team_id)
top_url = "https://{}.cloudforce.com/home/home.jsp".format(team_id)

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size={},{}".format(width,height))
driver = webdriver.Chrome(chrome_options=options)

# login
driver.get(login_url)
driver.implicitly_wait(10)
time.sleep(10)
uid = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
uid.send_keys(user_id)
password.send_keys(user_pass)
driver.find_element_by_id("Login").click()
time.sleep(10)

# attendance
driver.get(top_url)
time.sleep(10)
iframe = driver.find_element_by_xpath("//iframe[@title='AtkWorkComponent']")
driver.switch_to_frame(iframe)
time.sleep(5)
try:
    in_button = driver.find_element_by_xpath("//div[@id='btnStInput']")
    class_attr = in_button.get_attribute("class")
    if "pw_btnnst_dis" in class_attr:
        print("出勤不可")
    else:
        print("出勤")
        in_button.click()
        time.sleep(10)
except NoSuchElementException:
    print("出勤ボタンなし")

driver.quit()
