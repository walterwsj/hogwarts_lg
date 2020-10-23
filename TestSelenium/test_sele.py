from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time


class TestDemon():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_case(self):
        # self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("所有分类").click()
        my_class = self.driver.find_element_by_link_text("所有分类").get_attribute('class')
        assert "active" == my_class
