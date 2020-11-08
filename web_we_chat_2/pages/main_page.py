from selenium.webdriver.common.by import By

from hogwarts_lg.web_we_chat_2.pages.contact_page import ContactPage
from hogwarts_lg.web_we_chat_2.utility.base_test import BaseTest


class MainPage(BaseTest):
    def go_to_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg ww_indexImg_AddMember").click()
        return ContactPage(self.driver)

    def go_to_contact_page(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        return ContactPage(self.driver)
