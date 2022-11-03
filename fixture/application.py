from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def login(self, username, password):
        wd = self.wd
        # Open home page - 'Addressbook'
        self.open_home_page()
        # Login to 'Addressbook' as 'admin'
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("%s" % username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("%s" % password)
        wd.find_element("id", "LoginForm").submit()

    def logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "groups").click()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element("link text", "group page").click()

    def create_new_group(self, group):
        # Open groups page
        wd = self.wd
        self.open_groups_page()
        wd.find_element("name", "new").click()
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys("%s" % group.group_name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys("%s" % group.header_name)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys("%s" % group.footer_name)
        wd.find_element("name", "submit").click()
        # Return to group page
        self.return_to_group_page()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            alert = self.wd.switch_to.alert
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tear_down(self):
        self.wd.quit()
