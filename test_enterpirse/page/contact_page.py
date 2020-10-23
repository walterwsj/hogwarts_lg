from hogwarts_lg.test_enterpirse.page.add_member_page import AddMember
from hogwarts_lg.test_enterpirse.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_member(self):
        return AddMember(self.driver)
