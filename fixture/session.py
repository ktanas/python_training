class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd

        # Open home page - 'Addressbook'
        self.app.open_home_page()

        # Login to 'Addressbook' page
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("%s" % username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("%s" % password)
        wd.find_element("id", "LoginForm").submit()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()

    def logout_is_visible(self):
        wd = self.app.wd
        return len(wd.find_elements("link text", "Logout")) > 0

    def is_logged_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element("xpath", "//div/div[1]/form/b").text[1:-1]

    def ensure_logout(self):
        wd = self.app.wd
        if self.logout_is_visible():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.logout_is_visible():
            if self.is_logged_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
