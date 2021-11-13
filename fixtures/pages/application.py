from fixtures.pages.login import LoginPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)

    def quit(self):
        self.driver.quit()

    def open_login_page(self):
        self.driver.get(self.url)
