from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    first_button = browser.find_element_by_css_selector('button[type="submit"]').click()
    acsseet = browser.switch_to.alert.accept()
    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(5)
    browser.quit()
