# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from contact_utilities import *
from contact import *


class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):

        con = Contact (firstname="John",
                       middlename="Paul",
                       lastname="Smith",
                       nickname="Tiger",
                       photo_file_location="C:\\users\\ktana\\PyCharmProjects\\python_training\\aircraft_engine.JPG",
                       title="Senior Production Engineer",
                       company="J&S Machinery Inc.",
                       address="123 White Street\n00-123 Chicago, Illinois\nUnited States",
                       home_phone="123456789",
                       mobile_phone="234567890",
                       work_phone="345678901",
                       fax="456789012",
                       email="jsmith@jsmachinery.com",
                       email2="xxx@yyy.zzz.com",
                       email3="abc123@abc.com",
                       home_page="https://www.jsmachinery.com/~jsmith",
                       birth_day="1",
                       birth_month="January",
                       birth_year="1970",
                       anniversary_day="31",
                       anniversary_month="December",
                       anniversary_year="1992",
                       group_name="[none]",
                       extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
                       extra_phone="the same address as above",
                       notes="A nice record to test in Python!")

        wd = self.wd
        self.open_home_page()

        self.login(wd, user="admin", password="secret")

        self.go_to_new_contact_editor_page(wd)

        self.enter_contact_personal_data(wd, con)
#                                         firstname="John",
#                                         middlename="Paul",
#                                         lastname="Smith",
#                                         nickname="Tiger")
        self.enter_contact_photo(wd, con)
#                                 photo_file_location="C:\\users\\ktana\\PyCharmProjects\\python_training\\aircraft_engine.JPG")
        self.enter_contact_company_data(wd, con)
#                                        title="Senior Production Engineer",
#                                        company="J&S Machinery Inc.",
#                                        address="123 White Street\n00-123 Chicago, Illinois\nUnited States")
        self.enter_contact_phones(wd, con)
#                                  home_phone="123456789",
#                                  mobile_phone="234567890",
#                                  work_phone="345678901",
#                                  fax="456789012")
        self.enter_contact_email_addresses(wd, con)
#                                           email="jsmith@jsmachinery.com",
#                                           email2="xxx@yyy.zzz.com",
#                                           email3="abc123@abc.com")
        self.enter_contact_home_page(wd, con)
#                                     home_page="https://www.jsmachinery.com/~jsmith")
        self.enter_contract_dates(wd, con)
#                                  birth_day="1",
#                                  birth_month="January",
#                                  birth_year="1970",
#                                  anniversary_day="31",
#                                  anniversary_month="December",
#                                  anniversary_year="1992")
        self.enter_contact_group(wd, con)
#                                 group_name="[none]")
        self.enter_contact_extra_data(wd, con)
#                                      extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
#                                      extra_phone="the same address as above",
#                                      notes="A nice record to test in Python!")
        self.finalize_new_contact_addition(wd)
        self.logout(wd)

    def finalize_new_contact_addition(self, wd):
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()

    def enter_contact_extra_data(self, wd, contact):
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys("%ss" % contact.extra_address)
        wd.find_element("name", "phone2").click()
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys("%s" % contact.extra_phone)
        wd.find_element("name", "notes").click()
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys("%s" % contact.notes)

    def enter_contact_group(self, wd, contact):
        wd.find_element("name", "new_group").click()
        wd.find_element("xpath", "//option[@value='%s']" % contact.group_name).click()


    def enter_contract_dates(self, wd, contact):
        wd.find_element("name", "bday").click()
        Select(wd.find_element("name", "bday")).select_by_visible_text("%s" % contact.birth_day)
        wd.find_element("xpath", "//option[@value='" + contact.birth_day + "']").click()
        wd.find_element("name", "bmonth").click()
        Select(wd.find_element("name", "bmonth")).select_by_visible_text("%s" % contact.birth_month)
        wd.find_element("xpath", "//option[@value='"+ contact.birth_month +"']").click()
        wd.find_element("name", "byear").click()
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys("%s" % contact.birth_year)
        wd.find_element("name", "aday").click()
        Select(wd.find_element("name", "aday")).select_by_visible_text("%s" % contact.anniversary_day)
        shifted_aday = int(contact.anniversary_day)+2
        wd.find_element("xpath", "//div[@id='content']/form/select[3]/option["+ str(shifted_aday) +"]").click()
        wd.find_element("name", "amonth").click()
        Select(wd.find_element("name", "amonth")).select_by_visible_text("%s" % contact.anniversary_month)
        month_string = str(get_option_number_for_month(contact.anniversary_month)+2)
        wd.find_element("xpath", "//div[@id='content']/form/select[4]/option["+ month_string +"]").click()
        wd.find_element("name", "ayear").click()
        wd.find_element("name", "ayear").clear()
        wd.find_element("name", "ayear").send_keys("%s" % contact.anniversary_year)

    def enter_contact_home_page(self, wd, contact):
        wd.find_element("name", "homepage").click()
        wd.find_element("name", "homepage").clear()
        wd.find_element("name", "homepage").send_keys("%s" % contact.home_page)

    def enter_contact_email_addresses(self, wd, contact):
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys("%s" % contact.email)
        wd.find_element("name", "email2").click()
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys("%s" % contact.email2)
        wd.find_element("name", "email3").click()
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys("%s" % contact.email3)

    def enter_contact_phones(self, wd, contact):
        wd.find_element("name", "home").click()
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys("%s" % contact.home_phone)
        wd.find_element("name", "mobile").click()
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys("%s" % contact.mobile_phone)
        wd.find_element("name", "work").click()
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys("%s" % contact.work_phone)
        wd.find_element("name", "fax").click()
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys("%s" % contact.fax)

    def enter_contact_company_data(self, wd, contact):
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys("%s" % contact.title)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys("%s" % contact.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys("%s" % contact.address)

    def enter_contact_photo(self, wd, contact):
        #wd.find_element("name", "photo").click()
        wd.find_element("name", "photo").clear()
        wd.find_element("name", "photo").send_keys("%s" % contact.photo_file_location)

    def enter_contact_personal_data(self, wd, contact):
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys("%s" % contact.firstname)
        wd.find_element("name", "middlename").click()
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys("%s" % contact.middlename)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys("%s" % contact.lastname)
        wd.find_element("name", "nickname").click()
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys("%s" % contact.nickname)

    def go_to_new_contact_editor_page(self, wd):
        wd.find_element("link text", "add new").click()

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()


    def login(self, wd, user, password):
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("%s" % user)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("%s" % password)
        wd.find_element("id", "LoginForm").submit()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

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
