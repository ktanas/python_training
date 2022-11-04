# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application_group import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tear_down)
    return fixture


def test_group_add_test5(app):
    # Login to 'Addressbook' as 'admin'
    app.login(username="admin", password="secret")

    # Create a new group
    app.create_new_group(Group(group_name="Group1", header_name="Header1", footer_name="Footer1"))

    # Create a second, empty group
    app.create_new_group(Group(group_name="", header_name="", footer_name=""))

    # Logout
    app.logout()