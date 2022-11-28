from model.contact import *


def test_add_empty_contact(app):

    old_contacts = app.contact_data.get_contact_list()

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

    # This delay is necessary to give the application enough time to load.
    # Without this delay, this particular test fails, because the 'home' button on the upper toolbar of the
    # 'Addressbook' page is not visible when 'app.open_contact_home_page()' function is performed.
    app.delay(1)

    app.open_contact_home_page()

    app.go_to_new_contact_editor_page()

    app.contact_data.finalize_new_contact_addition()

    app.contact_data.return_to_home_page()

    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts) + 1

    old_contacts.append(con)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)
