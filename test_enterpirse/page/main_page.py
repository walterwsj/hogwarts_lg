from selenium.webdriver.common.by import By

from hogwarts_lg.test_enterpirse.page.add_member_page import AddMember
from hogwarts_lg.test_enterpirse.page.base_page import BasePage
from hogwarts_lg.test_enterpirse.page.contact_page import ContactPage


class MainPage(BasePage):
    def go_to_contact(self):
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR,"[node-type='addmember']").click()
        return AddMember(self.driver)
