def test_delete_first_group(app):
    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    # Delete first group in the list
    app.group.delete_first_group()

    # Return to the group page
    # app.group.return_to_group_page()

    # Logout
    app.session.logout()
