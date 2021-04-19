from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):       # вызывается каждый раp для всех тестов, перед началом выполнения
        print("\nstart browser for test suite........first")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):     # вызывается каждый раз для всех тестов, по факту выполнения последнего
        print("quit browser for test suite.......first")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print("lol")
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print("bet")
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")