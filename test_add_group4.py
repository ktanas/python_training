# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class GroupAddTest3(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_group_add_test2(self):
        # Open the AddressBook page
        wd = self.wd
        self.open_home_page(wd)

        self.login(wd, username="admin", password="secret")

        # Open groups page
        self.open_groups_page(wd)

        # Create a new group
        self.create_new_group(wd, Group(group_name="Group1", header_name="Header1", footer_name="Footer1"))

        # Check if our new group has been created
        self.check_if_new_group_was_created(wd)

        # Create a new group
        self.create_new_group(wd, Group(group_name="", header_name="", footer_name=""))

        # Check if our new group has been created
        self.check_if_new_group_was_created(wd)

        # Logout
        self.logout(wd)

    def check_if_new_group_was_created(self, wd):
        wd.find_element("link text", "group page").click()

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def open_groups_page(self, wd):
        wd.find_element("link text", "groups").click()

    def create_new_group(self, wd, group):
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

    def login(self, wd, username, password):
        # Login to 'Addressbook' as 'admin'
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("%s" % username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("%s" % password)
        wd.find_element("id", "LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: alert = self.wd.switch_to.alert
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
