def test_delete_first_contact(app):

    if app.contact_data.count() == 0:
        # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
        app.open_contact_home_page()
        app.go_to_new_contact_editor_page()
        app.contact_data.finalize_new_contact_addition()
        app.contact_data.return_to_home_page()

    app.open_contact_home_page()

    app.contact_data.delete_first_contact()

    app.open_contact_home_page()

    # Return to page with contacts, then logout
    #app.contact_data.return_to_home_page2()
