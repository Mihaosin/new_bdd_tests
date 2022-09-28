from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        # этот конструктор получает в качестве внешнего параметра ссылку на объект класса Application
        # и сохраняет ее в свойство с именем app
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        # авторизация в учетной записи
        wd.find_element(by=By.NAME, value="user").click()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.NAME, value="pass").click()
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.CSS_SELECTOR, value="input[value='Login']").click()

    def logout(self):
        wd = self.app.wd
        # выход из учетной записи
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(by=By.LINK_TEXT, value="Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_loggeg_in_user() == username

    def get_loggeg_in_user(self):
        wd = self.app.wd
        return wd.find_element(by=By.XPATH, value="//div[@id='top']/form/b").text[1:-1]

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)