from selenium import webdriver
from time import sleep
import math
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser.get(link)
button = browser.find_element_by_tag_name("button.trollface")
button.click()
second = browser.window_handles[1]
browser.switch_to.window(second)
x = browser.find_element_by_css_selector('span[id="input_value"]').text
answer = browser.find_element_by_id('answer')
answer.send_keys(calc(x))

button = browser.find_element_by_css_selector("button.btn")
button.click()
sleep(5)

browser.quit()