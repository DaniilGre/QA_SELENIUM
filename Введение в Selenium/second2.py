from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/selects1.html'


try:
    browser.get(link)
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    select = Select(browser.find_element_by_css_selector('select[id="dropdown"]'))
    lol = int(num1)+int(num2)
    select.select_by_value(str(lol))
finally:
    time.sleep(7)
    browser.quit()