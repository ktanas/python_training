def test_delete_first_group(app):
    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    # Delete first group in the list
    app.group.delete_first_group()

    # Logout
    app.session.logout()
