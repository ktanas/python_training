# -*- coding: utf-8 -*-
from model.group import Group


def test_add_empty_group(app):
    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    # Create an empty group
    app.group.create(Group(group_name="", header_name="", footer_name=""))

    # Logout
    app.session.logout()
