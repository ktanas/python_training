from random import randrange
from model.contact import Contact
import pytest


def test_delete_contact(app):

    with pytest.allure.step('Given a non-empty list of contacts'):

        old_contacts = app.contact_data.get_contact_list()

        if app.contact_data.count() == 0:
            # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
            app.open_contact_home_page()
            app.go_to_new_contact_editor_page()
            app.contact_data.finalize_new_contact_addition()
            app.contact_data.return_to_home_page()

            app.open_contact_home_page()

    with pytest.allure.step('Given index of a random contact from the list'):
        index = randrange(len(old_contacts))

    with pytest.allure.step('When I delete the contact from the list'):
        app.contact_data.delete_contact_by_index(index)
        app.open_contact_home_page()

    with pytest.allure.step('Then the new contact list is equal to old contact list without the deleted contact'):
        new_contacts = app.contact_data.get_contact_list()

        assert len(new_contacts) == len(old_contacts) - 1
        old_contacts[index:index+1] = []
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)
