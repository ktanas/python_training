from utilities.contact_utilities import *
from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def enter_text_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys("%s" % text)

    def enter_selectable_field_value(self, field_name, xpath, chosen_value):
        wd = self.app.wd
        if chosen_value is not None:
            wd.find_element("name", field_name).click()
            Select(wd.find_element("name", field_name)).select_by_visible_text("%s" % chosen_value)
            wd.find_element("xpath", xpath).click()

    def enter_contact_personal_data(self, contact):
        self.enter_text_field_value("firstname", contact.firstname)
        self.enter_text_field_value("middlename", contact.middlename)
        self.enter_text_field_value("lastname", contact.lastname)
        self.enter_text_field_value("nickname", contact.nickname)

    def enter_contact_photo(self, contact):
        if contact.photo_file_location is not None:
            wd = self.app.wd
            wd.find_element("name", "photo").clear()
            wd.find_element("name", "photo").send_keys("%s" % contact.photo_file_location)

    def enter_contact_company_data(self, contact):
        self.enter_text_field_value("title", contact.title)
        self.enter_text_field_value("company", contact.company)
        self.enter_text_field_value("address", contact.address)

    def enter_contact_phones(self, contact):
        self.enter_text_field_value("home", contact.home_phone)
        self.enter_text_field_value("mobile", contact.mobile_phone)
        self.enter_text_field_value("work", contact.work_phone)
        self.enter_text_field_value("fax", contact.fax)

    def enter_contact_email_addresses(self, contact):
        self.enter_text_field_value("email", contact.email)
        self.enter_text_field_value("email2", contact.email2)
        self.enter_text_field_value("email3", contact.email3)

    def enter_contact_home_page(self, contact):
        self.enter_text_field_value("homepage", contact.home_page)

    def enter_contract_dates(self, contact):
        self.enter_selectable_field_value("bday", "//option[@value='" + contact.birth_day + "']", contact.birth_day)
        self.enter_selectable_field_value("bmonth", "//option[@value='" + contact.birth_month + "']", contact.birth_month)
        self.enter_text_field_value("byear", contact.birth_year)
        self.enter_text_field_value("ayear", contact.anniversary_year)

        wd = self.app.wd

        if contact.anniversary_day is not None:
            wd.find_element("name", "aday").click()
            Select(wd.find_element("name", "aday")).select_by_visible_text("%s" % contact.anniversary_day)
            shifted_aday = int(contact.anniversary_day)+2
            wd.find_element("xpath", "//div[@id='content']/form/select[3]/option["+ str(shifted_aday) +"]").click()

        if contact.anniversary_month is not None:
            wd.find_element("name", "amonth").click()
            Select(wd.find_element("name", "amonth")).select_by_visible_text("%s" % contact.anniversary_month)
            month_string = str(get_option_number_for_month(contact.anniversary_month)+2)
            wd.find_element("xpath", "//div[@id='content']/form/select[4]/option["+ month_string +"]").click()

    def enter_contact_extra_data(self, contact):
        self.enter_text_field_value("address2", contact.extra_address)
        self.enter_text_field_value("phone2", contact.extra_phone)
        self.enter_text_field_value("notes", contact.notes)

    def enter_contact_group(self, contact):
        if contact.group_name is not None:
            wd = self.app.wd
            wd.find_element("name", "new_group").click()
            wd.find_element("xpath", "//option[@value='%s']" % contact.group_name).click()

    def finalize_new_contact_addition(self):
        wd = self.app.wd
        wd.find_element("xpath", "//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def modify_initialize(self):
        # Open page containing list of contacts
        wd = self.app.wd
        self.app.open_contact_home_page()

        # Select the first contact in the contact list
        wd.find_element("name", "selected[]").click()

        # Click on the edit icon (pencil) for the first contact
        wd.find_element("xpath", "//img[@alt='Edit']").click()

    def modify_finalize(self):
        # Click on the "Update" button after finishing modification of the contact's data
        wd = self.app.wd
        wd.find_element("name", "update").click()
        self.contact_cache = None

    def count(self):
        # Return number of currently existing contacts
        wd = self.app.wd
        return len(wd.find_elements("name", "selected[]"))

    def delete_first_contact(self):
        wd = self.app.wd
        # Select first contact in the contact list
        wd.find_element("name", "selected[]").click()
        # Delete the selected contact
        wd.find_element("xpath", "//input[@value='Delete']").click()

        # Confirm deletion of the contact and click 'OK' which is the alert acceptance button
        alert = wd.switch_to.alert

        if alert.text == "Delete 1 addresses?":
            alert.accept()
            self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_contact_home_page()
            self.contact_cache = []
            for element in wd.find_elements("name", "entry"):

                selectStr = element.find_element("name", "selected[]").get_attribute("title")
                cutStr = selectStr[selectStr.find('(')+1:selectStr.find(')')]
                firstNameStr = cutStr[0:cutStr.find(' ')]
                lastNameStr = cutStr[cutStr.find(' ')+1:len(cutStr)]
                id = element.find_element("name", "selected[]").get_attribute("value")

                self.contact_cache.append(Contact(firstname=firstNameStr, lastname=lastNameStr, id=id))
        return list(self.contact_cache)
