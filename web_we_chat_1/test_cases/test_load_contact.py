import time

from selenium import webdriver
import shelve

from selenium.webdriver.common.by import By

path = r'C:\Python3.6\contact.xlsx'


class TestLoadContact:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()

    def test_load_contact(self):
        file = shelve.open('../myDB/login_cookies')
        cookies = file['cookie']
        file.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        for cookie in cookies:
            if 'expiry' in cookie:
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.CSS_SELECTOR, "a[node-type='import']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(path)
        assert "contact.xlsx" == self.driver.find_element(By.CSS_SELECTOR,
                                                          '.ww_fileImporter_fileContainer_fileNames').text

    def test_load_cookie_to_db(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        while True:
            if r'https://work.weixin.qq.com/wework_admin/loginpage_wx' in self.driver.current_url:
                time.sleep(5)
            else:
                break
        cookies = self.driver.get_cookies()
        file = shelve.open("../myDB/login_cookies")
        file['cookie'] = cookies
        print(file['cookie'])
        file.close()
