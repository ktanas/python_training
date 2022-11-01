from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact_utilities import *


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

    def login(self, user, password):
        wd = self.wd
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys("%s" % user)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys("%s" % password)
        wd.find_element("id", "LoginForm").submit()

    def go_to_new_contact_editor_page(self):
        wd = self.wd
        wd.find_element("link text", "add new").click()

    def enter_contact_personal_data(self, contact):
        wd = self.wd
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

    def enter_contact_photo(self, wd, contact):
        wd = self.wd
        wd.find_element("name", "photo").clear()
        wd.find_element("name", "photo").send_keys("%s" % contact.photo_file_location)

    def enter_contact_company_data(self, contact):
        wd = self.wd
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys("%s" % contact.title)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys("%s" % contact.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys("%s" % contact.address)

    def enter_contact_phones(self, contact):
        wd = self.wd
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

    def enter_contact_email_addresses(self, contact):
        wd = self.wd
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys("%s" % contact.email)
        wd.find_element("name", "email2").click()
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys("%s" % contact.email2)
        wd.find_element("name", "email3").click()
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys("%s" % contact.email3)

    def enter_contact_home_page(self, contact):
        wd = self.wd
        wd.find_element("name", "homepage").click()
        wd.find_element("name", "homepage").clear()
        wd.find_element("name", "homepage").send_keys("%s" % contact.home_page)

    def enter_contract_dates(self, contact):
        wd = self.wd
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

    def enter_contact_group(self, contact):
        wd = self.wd
        wd.find_element("name", "new_group").click()
        wd.find_element("xpath", "//option[@value='%s']" % contact.group_name).click()

    def finalize_new_contact_addition(self):
        wd = self.wd
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()

    def enter_contact_extra_data(self, contact):
        wd = self.wd
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys("%ss" % contact.extra_address)
        wd.find_element("name", "phone2").click()
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys("%s" % contact.extra_phone)
        wd.find_element("name", "notes").click()
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys("%s" % contact.notes)

    def logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

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
