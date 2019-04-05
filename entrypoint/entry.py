# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import os
import time
import argparse

parser = argparse.ArgumentParser(description="Clocks in or out of TeamSpirit")
parser.add_argument("-u", "--username", dest="user_id", help="TeamSpirit username", required=True)
parser.add_argument("-p", "--password", dest="user_pass", help="TeamSpirit password", required=True)
parser.add_argument("-t", "--team-id", dest="team_id", help="TeamSpirit Team ID", default="teamspirit-2652")

args = parser.parse_args()
width = os.getenv("BROWSER_WIDTH", None)
height = os.getenv("BROWSER_HEIGHT", None)
team_id = args.team_id
user_id = args.user_id
user_pass = args.user_pass

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
clock_in_tab = driver.find_element_by_id("publisherAttach09D10000000CJm4")
clock_in_tab.click()
iframe = driver.find_element_by_xpath("//iframe[@title='Ts1PushTimeView']")
driver.switch_to_frame(iframe)
time.sleep(5)
out_button = driver.find_element_by_id("pushStart")
out_button.click()

driver.quit()
