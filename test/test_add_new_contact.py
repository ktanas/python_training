from model.contact import *
import pytest


def test_add_new_contact(app, json_contacts):

    # Extra test added for purpose of testing Allure framework
    # This test operates on a simplified contact, containing only the firstname, middlename, lastname and nickname

    contact = json_contacts

    with pytest.allure.step('Given a list of contacts'):
        old_contacts = app.contact_data.get_contact_list()

    with pytest.allure.step('Given a new contact %s with <firstname>, <middlename>, <lastname> and <nickname>' % contact):
        con = contact

    with pytest.allure.step('When I add new contact to the contact list'):
        # This delay is necessary to give the application enough time to load.
        # Without this delay, this particular test fails, because the 'home' button on the upper toolbar of the
        # 'Addressbook' page is not visible when 'app.open_contact_home_page()' function is performed.
        app.delay(1)

        app.open_contact_home_page()
        app.go_to_new_contact_editor_page()

        app.contact_data.enter_contact_personal_data(con)
        app.contact_data.finalize_new_contact_addition()

    with pytest.allure.step('Then the new contact list is equal to the old contact list with new contact'):
        new_contacts = app.contact_data.get_contact_list()

        assert len(new_contacts) == len(old_contacts) + 1
        old_contacts.append(con)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
