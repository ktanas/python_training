from model.contact import Contact


def test_delete_first_contact(app):

    old_contacts = app.contact_data.get_contact_list()

    if app.contact_data.count() == 0:
        # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
        app.open_contact_home_page()
        app.go_to_new_contact_editor_page()
        app.contact_data.finalize_new_contact_addition()
        app.contact_data.return_to_home_page()

    app.open_contact_home_page()

    app.contact_data.delete_first_contact()

    app.open_contact_home_page()

    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts) - 1

    old_contacts.append(Contact(firstname="", lastname=""))

    # Return to page with contacts, then logout
    #app.contact_data.return_to_home_page2()
