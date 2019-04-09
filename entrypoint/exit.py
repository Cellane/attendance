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
print("starting with team id: {}, username: {}, password: {}".format(team_id, user_id, user_pass))

login_url = "https://{}.cloudforce.com/".format(team_id)
top_url = "https://{}.cloudforce.com/home/home.jsp".format(team_id)

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size={},{}".format(width,height))
driver = webdriver.Chrome(chrome_options=options)
print("driver initialized")

# login
driver.get(login_url)
driver.implicitly_wait(10)
time.sleep(10)
print("navigated to login page: {}".format(driver.current_url))

uid = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
print("login inputs found: username: {}, password: {}".format(uid, password))

uid.send_keys(user_id)
password.send_keys(user_pass)
print("credentials filled in")

login_button = driver.find_element_by_id("Login")
print("login button found: {}", login_button)

login_button.click()
print("login button clicked")

driver.implicitly_wait(10)
time.sleep(10)
print("current url: {}".format(driver.current_url))

# attendance
driver.get(top_url)
driver.implicitly_wait(10)
time.sleep(10)
print("navigated to top url: {}".format(top_url))

clock_in_tab = driver.find_element_by_id("publisherAttach09D10000000CJm4")
print("clock in tab found: {}".format(clock_in_tab))

clock_in_tab.click()
print("clock in tab clicked")

iframe = driver.find_element_by_xpath("//iframe[@title='Ts1PushTimeView']")
print("clock in iframe found: {}".format(iframe))

driver.switch_to_frame(iframe)
driver.implicitly_wait(10)
time.sleep(10)

attendance_button = driver.find_element_by_id("pushEnd")
print("in/out button found: {}".format(attendance_button))

attendance_button.click()
driver.implicitly_wait(10)
time.sleep(10)
print("in/out button clicked")

driver.quit()
print("quitting…")
