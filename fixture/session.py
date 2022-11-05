class SessionHelper:

    def __init__(self,app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd

        # Open home page - 'Addressbook'
        self.app.open_home_page()

        # Login to 'Addressbook' as 'admin'
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("%s" % username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("%s" % password)
        wd.find_element("id", "LoginForm").submit()

    def logout(self):
        wd = self.app.wd
        wd.find_element("link text", "Logout").click()
