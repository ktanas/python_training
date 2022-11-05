# -*- coding: utf-8 -*-
import pytest

from model.contact import *
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tear_down)
    return fixture


def test_add_contact3(app):

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

    app.open_home_page()

    app.login(user="admin", password="secret")

    app.go_to_new_contact_editor_page()

    app.enter_contact_personal_data(con)
#                                         firstname="John",
#                                         middlename="Paul",
#                                         lastname="Smith",
#                                         nickname="Tiger")
    app.enter_contact_photo(con)
#                                 photo_file_location="C:\\users\\ktana\\PyCharmProjects\\python_training\\aircraft_engine.JPG")
    app.enter_contact_company_data(con)
#                                        title="Senior Production Engineer",
#                                        company="J&S Machinery Inc.",
#                                        address="123 White Street\n00-123 Chicago, Illinois\nUnited States")
    app.enter_contact_phones(con)
#                                  home_phone="123456789",
#                                  mobile_phone="234567890",
#                                  work_phone="345678901",
#                                  fax="456789012")
    app.enter_contact_email_addresses(con)
#                                           email="jsmith@jsmachinery.com",
#                                           email2="xxx@yyy.zzz.com",
#                                           email3="abc123@abc.com")
    app.enter_contact_home_page(con)
#                                     home_page="https://www.jsmachinery.com/~jsmith")
    app.enter_contract_dates(con)
#                                  birth_day="1",
#                                  birth_month="January",
#                                  birth_year="1970",
#                                  anniversary_day="31",
#                                  anniversary_month="December",
#                                  anniversary_year="1992")
    app.enter_contact_group(con)
#                                 group_name="[none]")
    app.enter_contact_extra_data(con)
#                                      extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
#                                      extra_phone="the same address as above",
#                                      notes="A nice record to test in Python!")
    app.finalize_new_contact_addition()
    app.logout()


def test_add_empty_contact(app):

    con = Contact(firstname="",
                  middlename="",
                  lastname="",
                  nickname="",
                  photo_file_location="",
                  title="",
                  company="",
                  address="",
                  home_phone="",
                  mobile_phone="",
                  work_phone="",
                  fax="",
                  email="",
                  email2="",
                  email3="",
                  home_page="",
                  birth_day="",
                  birth_month="",
                  birth_year="",
                  anniversary_day="",
                  anniversary_month="",
                  anniversary_year="",
                  group_name="",
                  extra_address="",
                  extra_phone="",
                  notes="")

    app.open_home_page()

    app.login(user="admin", password="secret")

    app.go_to_new_contact_editor_page()

#    app.enter_contact_personal_data(con)

#    app.enter_contact_photo(con)

#    app.enter_contact_company_data(con)

#    app.enter_contact_phones(con)

#    app.enter_contact_email_addresses(con)

#    app.enter_contact_home_page(con)

#    app.enter_contract_dates(con)

#    app.enter_contact_group(con)

#    app.enter_contact_extra_data(con)

    app.finalize_new_contact_addition()

    app.logout()
