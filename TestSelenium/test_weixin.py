import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time


class TestWeixin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        option = Options()
        option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_case(self):
        pass

    def test_cookie(self):
        self.driver.get("https://ceshiren.com/")

        with open('../web_we_chat_1/myDB/cookie.json', 'r') as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.find_element_by_link_text("所有分类").click()
        my_class = self.driver.find_element_by_link_text("所有分类").get_attribute('class')
        assert "active" == my_class

        # cookies = self.driver.get_cookies()
        # with open('cookie.json','w') as f:
        #     json.dump(cookies,f)


