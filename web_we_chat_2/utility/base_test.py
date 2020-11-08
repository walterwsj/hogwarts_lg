from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest:
    def __init__(self, base_obj=None):
        if base_obj is None:
            option = Options()
            option.debugger_address("localhost:9222")
            self.driver = webdriver.Chrome(options=option)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver = base_obj
        self.driver.implicitly_wait(5)
