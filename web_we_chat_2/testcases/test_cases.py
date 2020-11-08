from selenium.webdriver.common.by import By

from hogwarts_lg.web_we_chat_2.pages.main_page import MainPage


class TestCase:
    def test_add_depart(self):
        self.main = MainPage()
        res = self.main.go_to_contact_page().go_to_add_department().add_department("test").get_depart_name()
        assert "test" in res
