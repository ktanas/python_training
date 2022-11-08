def test_delete_first_contact(app):

    app.session.login(username="admin", password="secret")

    app.open_contact_home_page()

    app.contact_data.delete_first_contact()

    # Return to page with contacts, then logout
    app.contact_data.return_to_home_page2()
    app.session.logout()