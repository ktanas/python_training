# -*- coding: utf-8 -*-
from model.contact import *


def test_modify_first_contact(app):

    # Let us assume that we modify only the contact's first and last name and birthday
    # This is not a real-life project, just an exercise made during training
    # Implementing methods to change every possible data field in the contact would take way too much time

    # Edit the contact data

    con = Contact(firstname="Anne",
                  lastname="Jones",
                  birth_day="31",
                  birth_month="December",
                  birth_year="1999")

    app.session.login(username="admin", password="secret")

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

    app.session.logout()
