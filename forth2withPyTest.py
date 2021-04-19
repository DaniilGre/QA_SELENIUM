import pytest

from selenium import webdriver
import time


class TestMylesson:

    def test_first_reg(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('input.form-control.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
        input3.send_keys("stepik@gmail.com")
        button = browser.find_element_by_css_selector('button[type="submit"]')
        button.click()
        # закрываем браузер после всех манипуляций
        browser.quit()
        assert 10 == 10, 'lol'

    def test_socond_reg(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('input.form-control.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
        input3.send_keys("stepik@gmail.com")
        button = browser.find_element_by_css_selector('button[type="submit"]')
        button.click()
        # успеваем скопировать код за 10 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
        assert 10 == 11, 'lol'

