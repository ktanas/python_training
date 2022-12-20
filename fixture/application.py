from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self, browser="", base_url="", username="", password=""):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self, username, password)
        self.group = GroupHelper(self)
        self.contact_data = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def delay(self, time):
        wd = self.wd
        wd.implicitly_wait(time)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        return wd

    def open_contact_home_page(self):
        wd = self.wd
        if (len(wd.find_elements("link text", "Send e-Mail")) == 0
            or len(wd.find_elements("link text", "Delete")) == 0
            or len(wd.find_elements("link text", "Add to")) == 0):
                wd.find_element("link text", "home").click()

    def go_to_new_contact_editor_page(self):
        wd = self.wd
        wd.find_element("link text", "add new").click()

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
