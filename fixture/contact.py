from utilities.contact_utilities import *
from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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

    def enter_contact_dates(self, contact):
        self.enter_selectable_field_value("bday", "//option[@value='%s']" % contact.birth_day, contact.birth_day)
        self.enter_selectable_field_value("bmonth", "//option[@value='%s']" % contact.birth_month, contact.birth_month)
        self.enter_text_field_value("byear", contact.birth_year)
        self.enter_text_field_value("ayear", contact.anniversary_year)

        wd = self.app.wd

        if contact.anniversary_day is not None:
            wd.find_element("name", "aday").click()
            Select(wd.find_element("name", "aday")).select_by_visible_text("%s" % contact.anniversary_day)
            shifted_aday = int(contact.anniversary_day)+2
            wd.find_element("xpath", "//div[@id='content']/form/select[3]/option[%s]" % str(shifted_aday)).click()

        if contact.anniversary_month is not None:
            wd.find_element("name", "amonth").click()
            Select(wd.find_element("name", "amonth")).select_by_visible_text("%s" % contact.anniversary_month)
            month_string = str(get_option_number_for_month(contact.anniversary_month)+2)
            wd.find_element("xpath", "//div[@id='content']/form/select[4]/option[%s]" % month_string).click()

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

    def modify_initialize(self, index):
        # Open page containing list of contacts
        wd = self.app.wd
        self.app.open_contact_home_page()

        # Select contact with the given index in the contact list
        wd.find_element("name", "selected[]").click()

        # Click on the edit icon (pencil) for the first contact
        wd.find_elements("xpath", "//img[@alt='Edit']")[index].click()

    def modify_finalize(self):
        # Click on the "Update" button after finishing modification of the contact's data
        wd = self.app.wd
        wd.find_element("name", "update").click()
        self.contact_cache = None

    def count(self):
        # Return number of currently existing contacts
        wd = self.app.wd
        return len(wd.find_elements("name", "selected[]"))

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Select contact with the given index from the contact list
        wd.find_elements("name", "selected[]")[index].click()
        # Delete the selected contact
        wd.find_element("xpath", "//input[@value='Delete']").click()

        # Confirm deletion of the contact and click 'OK' which is the alert acceptance button
        alert = wd.switch_to.alert

        if alert.text == "Delete 1 addresses?":
            alert.accept()
            self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element("link text", "home page").click()

    contact_cache = None

    def get_contact_list_old(self):
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

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_contact_home_page()
            self.contact_cache = []
            for element in wd.find_elements("name", "entry"):

                cells = element.find_elements("tag name", "td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element("tag name", "input").get_attribute("value")
                all_phones = cells[5].text
                print("all_phones="+str(all_phones))
                all_emails = cells[4].text
                print("all_emails="+str(all_emails))
                address = cells[3].text

                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails,
                                                  address=address))
#                                                  home_phone=all_phones[0], mobile_phone=all_phones[1],
#                                                  work_phone=all_phones[2], extra_phone=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        # print("open_contact_to_edit_by_index:index=",index)
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements("name", "entry")[index]
        cell = row.find_elements("tag name", "td")[7]
        cell.find_element("tag name", "a").click()

    def open_contact_view_by_index(self, index):
        # print("open_contact_view_by_index:index=",index)
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements("name", "entry")[index]
        cell = row.find_elements("tag name", "td")[6]
        cell.find_element("tag name", "a").click()

    def get_contact_info_from_edit_page(self, index):
        # print("get_contact_info_from_edit_page:index=",index)
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element("name", "id").get_attribute("value")
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        middlename = wd.find_element("name", "middlename").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        home_phone = wd.find_element("name", "home").get_attribute("value")
        work_phone = wd.find_element("name", "work").get_attribute("value")
        mobile_phone = wd.find_element("name", "mobile").get_attribute("value")
        extra_phone = wd.find_element("name", "phone2").get_attribute("value")

        email = wd.find_element("name", "email").get_attribute("value")
        email2 = wd.find_element("name", "email2").get_attribute("value")
        email3 = wd.find_element("name", "email3").get_attribute("value")

        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, id=id,
                       address=address,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, extra_phone=extra_phone,
                       email=email, email2=email2, email3=email3)

    def get_firstname_of_given_contact_from_contact_list(self, index):
        # print("get_firstname_of_given_contact_from_contact_list:index=",index)
        wd = self.app.wd
        self.app.open_contact_home_page()
        cells = wd.find_elements("name", "entry")[index].find_elements("tag name", "td")
        return cells[2].text

    def get_lastname_of_given_contact_from_contact_list(self, index):
        # print("get_lastname_of_given_contact_from_contact_list:index=",index)
        wd = self.app.wd
        self.app.open_contact_home_page()
        cells = wd.find_elements("name", "entry")[index].find_elements("tag name", "td")
        return cells[1].text

    def get_contact_from_view_page(self, index):
        # print("get_contact_from_view_page:index=",index)
        wd = self.app.wd
        firstname = self.get_firstname_of_given_contact_from_contact_list(index)
        lastname = self.get_lastname_of_given_contact_from_contact_list(index)

        self.open_contact_view_by_index(index)
        text = wd.find_element("id", "content").text
        #print("get_contact_from_view_page: text="+text)

        l1 = len(firstname)
        l2 = len(lastname)
        middlename=""
        if l1+l2 > 0:
            fullname = text.splitlines()[0]
            if l1>0:
                if l2>0:
                    middlename=fullname[len(firstname)+1:len(fullname)-len(lastname)-1]
                else:
                    middlename=fullname[len(firstname)+1:len(fullname)]
            else:
                middlename=fullname[0:len(firstname)]

        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        extra_phone = re.search("P: (.*)", text).group(1)
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, extra_phone=extra_phone)
