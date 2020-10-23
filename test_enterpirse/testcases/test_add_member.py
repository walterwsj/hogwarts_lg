from hogwarts_lg.test_enterpirse.page.base_page import BasePage
from hogwarts_lg.test_enterpirse.page.main_page import MainPage


class TestAddMember:
    def test_add_member(self):
        self.main = MainPage()
        self.main.go_to_add_member().add_member()
