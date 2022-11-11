# -*- coding: utf-8 -*-

from model.contact import *


def test_add_contact(app):

    con = Contact(firstname="John",
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

    app.open_contact_home_page()

    app.go_to_new_contact_editor_page()

    app.contact_data.enter_contact_personal_data(con)
#                                         firstname="John",
#                                         middlename="Paul",
#                                         lastname="Smith",
#                                         nickname="Tiger")
    app.contact_data.enter_contact_photo(con)
#                                 photo_file_location="C:\\users\\ktana\\PyCharmProjects\\python_training\\aircraft_engine.JPG")
    app.contact_data.enter_contact_company_data(con)
#                                        title="Senior Production Engineer",
#                                        company="J&S Machinery Inc.",
#                                        address="123 White Street\n00-123 Chicago, Illinois\nUnited States")
    app.contact_data.enter_contact_phones(con)
#                                  home_phone="123456789",
#                                  mobile_phone="234567890",
#                                  work_phone="345678901",
#                                  fax="456789012")
    app.contact_data.enter_contact_email_addresses(con)
#                                           email="jsmith@jsmachinery.com",
#                                           email2="xxx@yyy.zzz.com",
#                                           email3="abc123@abc.com")
    app.contact_data.enter_contact_home_page(con)
#                                     home_page="https://www.jsmachinery.com/~jsmith")
    app.contact_data.enter_contract_dates(con)
#                                  birth_day="1",
#                                  birth_month="January",
#                                  birth_year="1970",
#                                  anniversary_day="31",
#                                  anniversary_month="December",
#                                  anniversary_year="1992")
    app.contact_data.enter_contact_group(con)
#                                 group_name="[none]")
    app.contact_data.enter_contact_extra_data(con)
#                                      extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
#                                      extra_phone="the same address as above",
#                                      notes="A nice record to test in Python!")
    app.contact_data.finalize_new_contact_addition()


