from selenium.webdriver.common.by import By

from hogwarts_lg.web_we_chat_2.pages.contact_page import ContactPage
from hogwarts_lg.web_we_chat_2.utility.base_test import BaseTest


class DepartPage(BaseTest):
    def add_department(self, depart_name):
        self.driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys(depart_name)
        self.driver.find_element(By.CSS_SELECTOR, "a[d_ck='submit']").Click()
        return ContactPage(self.driver)
