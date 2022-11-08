# -*- coding: utf-8 -*-

def test_modify_first_contact(app):

    # Let us assume that we modify only the contact's first and last name and birthday
    # This is not a real-life project, just an exercise made during training
    # Implementing methods to change every possible data field in the contact would take way too much time

    app.session.login(username="admin", password="secret")

    app.open_contact_home_page()

    # Edit the contact data
    app.contact_data.modify_initialize()
    app.contact_data.modify_first_name("Robert")
    app.contact_data.modify_last_name("Lewandowski")
    app.contact_data.modify_birthday("21", "August", "1988")
    app.contact_data.modify_finalize()

    # Return to page with contacts, then logout
    app.contact_data.return_to_home_page()
    app.session.logout()