from model.contact import *
import pytest
from random import randrange


def test_modify_contact(app, firstname, middlename, lastname, nickname):

    # Extra test added for purpose of testing Allure framework
    # This test operates on a simplified contact, containing only the firstname, middlename, lastname and nickname

    with pytest.allure.step('Given a non-empty list of contacts'):
        if app.contact_data.count() == 0:
            # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
            app.open_contact_home_page()
            app.go_to_new_contact_editor_page()
            app.contact_data.finalize_new_contact_addition()
            app.contact_data.return_to_home_page()

            old_contacts = app.contact_data.get_contact_list()

    with pytest.allure.step('Given index of a random contact from the list'):
        index = randrange(len(old_contacts))

    with pytest.allure.step('When a new <%s>, <%s>, <%s> and <%s> is entered' % firstname % middlename % lastname % nickname):
        con = Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname)
        con.id = old_contacts[index].id

        app.contact_data.modify_initialize(index)
        app.contact_data.enter_contact_personal_data(con)
        app.contact_data.modify_finalize()

    with pytest.allure.step('Then the new contact list is equal to old contact list with modified contact'):
        new_contacts = app.contact_data.get_contact_list()
        assert len(new_contacts) == len(old_contacts)
        old_contacts[index] = con
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
