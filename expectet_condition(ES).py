from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import math
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)
    button = browser.find_elements_by_css_selector("button.btn")
    button[0].location_once_scrolled_into_view
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    button[0].click()

    x = browser.find_element_by_css_selector('span[id="input_value"]').text
    answer = browser.find_element_by_id('answer')
    answer.send_keys(calc(x))
    button[1].location_once_scrolled_into_view
    button[1].click()

finally:
    sleep(5)
    browser.quit()