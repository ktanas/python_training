# -*- coding: utf-8 -*-
from model.contact import *


def test_modify_first_contact(app):

    if app.contact_data.count() == 0:
        # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
        app.open_contact_home_page()
        app.go_to_new_contact_editor_page()
        app.contact_data.finalize_new_contact_addition()
        app.contact_data.return_to_home_page()

    # Let us assume that we modify only the contact's first and last name and birthday
    # This is not a real-life project, just an exercise made during training
    # Implementing methods to change every possible data field in the contact would take way too much time

    old_contacts = app.contact_data.get_contact_list()

    # Edit the contact data

    con = Contact(firstname="Anne",
                  lastname="Jones",
                  birth_day="31",
                  birth_month="December",
                  birth_year="1999")

    con.id = old_contacts[0].id

    app.contact_data.modify_initialize()

    app.contact_data.enter_contact_personal_data(con)
    #                                         firstname="Anne",
    #                                         lastname="Jones",

    app.contact_data.enter_contact_photo(con)

    app.contact_data.enter_contact_company_data(con)

    app.contact_data.enter_contact_phones(con)

    app.contact_data.enter_contact_email_addresses(con)

    app.contact_data.enter_contact_home_page(con)

    app.contact_data.enter_contract_dates(con)
    #                                  birth_day="31",
    #                                  birth_month="December",
    #                                  birth_year="1999",
    app.contact_data.enter_contact_group(con)

    app.contact_data.enter_contact_extra_data(con)

    app.contact_data.modify_finalize()

    new_contacts = app.contact_data.get_contact_list()
    assert len(new_contacts) == len(old_contacts)

    old_contacts[0] = con

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)
