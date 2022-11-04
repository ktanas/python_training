# -*- coding: utf-8 -*-
import pytest

from fixture.application_contact import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tear_down)
    return fixture


def test_modify_first_contact(app):

    # Let us assume that we modify only the contact's first and last name and birthday
    # This is not a real-life project, just an exercise made during training
    # Implementing methods to change every possible data field in the contact would take way too much time

    app.open_home_page()

    app.session.login(user="admin", password="secret")

    app.open_contact_home_page()

    app.contact_data.modify_initialize()
    app.contact_data.modify_first_name("Robert")
    app.contact_data.modify_last_name("Lewandowski")
    app.contact_data.modify_birthday("21", "August", "1988")
    app.contact_data.modify_finalize()
    app.contact_data.return_to_home_page()

    app.session.logout()