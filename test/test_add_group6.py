# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tear_down)
    return fixture


def test_add_group(app):
    # Login to 'Addressbook' as 'admin'
    app.login(username="admin", password="secret")

    # Create a new group
    app.create_new_group(Group(group_name="Group1", header_name="Header1", footer_name="Footer1"))

    # Logout
    app.logout()


def test_add_empty_group(app):
    # Login to 'Addressbook' as 'admin'
    app.login(username="admin", password="secret")

    # Create an empty group
    app.create_new_group(Group(group_name="", header_name="", footer_name=""))

    # Logout
    app.logout()
