from selenium import webdriver
from time import sleep
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'txt.txt')           # добавляем к этому пути имя файла


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_css_selector('[name="firstname"]').send_keys("test")
    browser.find_element_by_css_selector('[name="lastname"]').send_keys("test")
    browser.find_element_by_css_selector('[name="email"]').send_keys("test")
    browser.find_element_by_css_selector('[name="file"]').send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.location_once_scrolled_into_view
    button.click()
finally:
    sleep(8)
    browser.quit()