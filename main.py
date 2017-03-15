#!/usr/local/bin/python3

from splinter import Browser
from selenium.webdriver.common.keys import Keys
from config import URL, USER, PASSWORD

import os
import time

with Browser('chrome') as browser:
    browser.visit(URL)

    if browser.status_code.is_success():
        browser.find_by_id('j_username').fill(USER)
        browser.find_by_id('j_password').fill(PASSWORD)
        browser.find_by_id('submit').click()

        browser.find_by_id('avatar-picker-button').click()

        (
            browser
                .driver
                .find_element_by_id('faux-upload-field-1')
                .send_keys(os.path.abspath('shopping-cart.png'))
        )

        image_size_slider = browser.driver.find_element_by_css_selector('.image-explorer-scale-slider')

        while int(image_size_slider.get_property('value')) > 0:
            image_size_slider.send_keys(Keys.ARROW_LEFT)

        browser.find_by_css('.avatar-picker-save').first.click()

        time.sleep(1)

        browser.find_by_id('submit').click()
