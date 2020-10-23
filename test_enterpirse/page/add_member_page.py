import time

from selenium.webdriver.common.by import By

from hogwarts_lg.test_enterpirse.page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.driver.find_element(By.ID, "username").send_keys("123")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("123")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("123")
        # driver.find_element_by_css_selector("")
        # driver.find_element_by_css_selector("")
        # driver.find_element_by_css_selector("")
