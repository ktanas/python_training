# -*- coding: utf-8 -*-

from model.contact import *
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(prefix, maxlen):
    return prefix + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def generate_random_valid_day():

    month = random.choice(months)
    year = random.randrange(1900, 2001)

    if month == "February":
        if (year % 4 > 0) or ((year % 100 == 0) and (year % 400 > 0)):
            day = random.randrange(1, 29) # 1..28
        else:
            day = random.randrange(1, 30) # 1..29
    elif month in ["April", "June", "September", "November"]:
        day = random.randrange(1, 31) # 1..30
    else:
        day = random.randrange(1, 32) # 1..31

    return [day, month, year]


birth_data = generate_random_valid_day()
anniversary_data = generate_random_valid_day()

testdata = [
       Contact(
           firstname=random_string("firstname", 15),
           middlename=middlename,
           lastname=random_string("lastname", 15),
           nickname=nickname,
           photo_file_location=photo_file_location,
           title="Senior Production Engineer",
           company="J&S Machinery Inc.",
           address="123 White Street\n00-123 Chicago, Illinois\nUnited States",
           home_phone=random_digits("home_phone", 9),
           mobile_phone=random_digits("mobile_phone", 9),
           work_phone=random_digits("work_phone", 9),
           fax=random_digits("fax", 10),
           email="jsmith@jsmachinery.com",
           email2="xxx@yyy.zzz.com",
           email3="abc123@abc.com",
           home_page="https://www.jsmachinery.com/~jsmith",
           birth_day=birth_data[0],
           birth_month=birth_data[1],
           birth_year=birth_data[2],
           anniversary_day=anniversary_data[0],
           anniversary_month=anniversary_data[1],
           anniversary_year=anniversary_data[2],
           group_name="[none]",
           extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
           extra_phone=random_digits("extra_phone", 9),
           notes="A nice record to test in Python!",
           id=id
       )
       for middlename in ["", random_string("middlename", 20)]
       for nickname in ["", random_string("nickname", 10)]
       for photo_file_location in ["", "C:\\users\\ktana\\PyCharmProjects\\python_training\\aircraft_engine.JPG"]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):

    old_contacts = app.contact_data.get_contact_list()

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
                  extra_phone="82828282",
                  notes="A nice record to test in Python!")

    # This delay is necessary to give the application enough time to load.
    # Without this delay, this particular test fails, because the 'home' button on the upper toolbar of the
    # 'Addressbook' page is not visible when 'app.open_contact_home_page()' function is performed.
    app.delay(1)

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
    app.contact_data.enter_contact_dates(con)
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

#################################################
    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts) + 1

    old_contacts.append(con)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)
