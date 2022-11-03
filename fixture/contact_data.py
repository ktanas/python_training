from utilities.contact_utilities import *
from selenium.webdriver.support.ui import Select


class ContactDataHelper:

    def __init__(self, app):
        self.app = app

    def enter_contact_personal_data(self, contact):
        wd = self.app.wd
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

    def enter_contact_photo(self, contact):
        wd = self.app.wd
        wd.find_element("name", "photo").clear()
        wd.find_element("name", "photo").send_keys("%s" % contact.photo_file_location)

    def enter_contact_company_data(self, contact):
        wd = self.app.wd
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
        wd = self.app.wd
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
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element("name", "homepage").click()
        wd.find_element("name", "homepage").clear()
        wd.find_element("name", "homepage").send_keys("%s" % contact.home_page)

    def enter_contract_dates(self, contact):
        wd = self.app.wd
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

    def enter_contact_extra_data(self, contact):
        wd = self.app.wd
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys("%ss" % contact.extra_address)
        wd.find_element("name", "phone2").click()
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys("%s" % contact.extra_phone)
        wd.find_element("name", "notes").click()
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys("%s" % contact.notes)

    def enter_contact_group(self, contact):
        wd = self.app.wd
        wd.find_element("name", "new_group").click()
        wd.find_element("xpath", "//option[@value='%s']" % contact.group_name).click()

    def finalize_new_contact_addition(self):
        wd = self.app.wd
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()
