# -*- coding: utf-8 -*-

from model.contact import *


def test_add_contact(app, json_contacts):

    contact = json_contacts

    old_contacts = app.contact_data.get_contact_list()

    con = contact

    # This delay is necessary to give the application enough time to load.
    # Without this delay, this particular test fails, because the 'home' button on the upper toolbar of the
    # 'Addressbook' page is not visible when 'app.open_contact_home_page()' function is performed.
    app.delay(1)

    app.open_contact_home_page()

    app.go_to_new_contact_editor_page()

    app.contact_data.enter_contact_personal_data(con)
    app.contact_data.enter_contact_photo(con)
    app.contact_data.enter_contact_company_data(con)
    app.contact_data.enter_contact_phones(con)
    app.contact_data.enter_contact_email_addresses(con)
    app.contact_data.enter_contact_home_page(con)
    app.contact_data.enter_contact_dates(con)
    app.contact_data.enter_contact_group(con)
    app.contact_data.enter_contact_extra_data(con)
    app.contact_data.finalize_new_contact_addition()

########################################################
    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts) + 1

    old_contacts.append(con)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)
