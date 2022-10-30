# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class GroupAddTest1(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_group_add_test1(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element("name","user").clear()
        wd.find_element("name","user").send_keys("admin")
        wd.find_element("name","pass").click()
        wd.find_element("name","pass").clear()
        wd.find_element("name","pass").send_keys("secret")
        wd.find_element("id","LoginForm").submit()
        wd.find_element("link text","groups").click()
        wd.find_element("name", "new").click()
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys("Group1")
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys("Header1")
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys("Footer1")
        wd.find_element("name", "submit").click()
        wd.find_element("link text","group page").click()
        wd.find_element("link text","Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: alert = self.wd.switch_to.alert
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()