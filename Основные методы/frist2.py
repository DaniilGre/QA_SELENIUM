from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    browser.find_element_by_css_selector('input[id="robotCheckbox"]').click()
    lol = browser.find_element_by_css_selector('input[id="robotsRule"]')
    lol.location_once_scrolled_into_view
    lol.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.location_once_scrolled_into_view
    button.click()
finally:
    time.sleep(5)
    browser.quit()
