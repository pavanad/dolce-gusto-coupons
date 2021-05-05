# -*- coding: utf-8 -*-

import time
from secrets import DOLCE_PASSWORD, DOLCE_USERNAME

from selenium import webdriver


def open_browser():
    url = "https://www.nescafe-dolcegusto.com.br/"
    browser = webdriver.Firefox()
    browser.get(url)

    browser.find_element_by_css_selector("a.my-account").click()

    username = browser.find_element_by_id("email")
    password = browser.find_element_by_id("pass")
    username.send_keys(DOLCE_USERNAME)
    password.send_keys(DOLCE_PASSWORD)
    browser.find_element_by_id("send2").click()
    browser.find_element_by_link_text("Meu Bônus").click()
    time.sleep(3)

    return browser
