from selenium.webdriver.common.by import By
from hogwarts_lg.web_we_chat_2.pages.department_page import DepartPage
from hogwarts_lg.web_we_chat_2.utility.base_test import BaseTest


class ContactPage(BaseTest):
    def go_to_add_department(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class='js_add_sub_party']").click()
        return DepartPage(self.driver)

    def get_depart_name(self):
        depart_list = self.driver.find_elements(By.CSS_SELECTOR, "a[class='jstree-anchor']")
        return [depart.text for depart in depart_list]
