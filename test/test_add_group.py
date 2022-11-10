# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    # Create a new group
    app.group.create(Group(group_name="Group1", header_name="Header1", footer_name="Footer1"))

    # Logout
    app.session.logout()
