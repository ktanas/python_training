from model.contact import Contact
from sys import maxsize
from random import randrange
from pytest_bdd import given, when, then, parsers


# Let us limit the contact's data to first,middle and last name, and nickname - entering all the contact's data fields
# would be too complicated. This is just an exercise done to understand idea of BDD testing, not a real-life project.
@given(parsers.parse('a new contact with {firstname}, {middlename}, {lastname} and {nickname}'),
       target_fixture='new_contact')
def new_contact(firstname, middlename, lastname, nickname):
    return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname)


@given('a list of contacts', target_fixture='contact_list')
def contact_list(app):
    contact_list = app.contact_data.get_contact_list()
    return contact_list

@given('a non-empty list of contacts', target_fixture='non_empty_contact_list')
def non_empty_contact_list(app):
    if len(app.contact_data.get_contact_list()) == 0:

        app.open_contact_home_page()
        app.go_to_new_contact_editor_page()

        con = Contact(firstname="", middlename="", lastname="", nickname="")

        app.contact_data.enter_contact_personal_data(con)
        app.contact_data.finalize_new_contact_addition()

        non_empty_contact_list = app.contact_data.get_contact_list()
        return non_empty_contact_list


@given('index of a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return randrange(len(non_empty_contact_list))


@when('I add new contact to the contact list')
def add_new_contact(app, new_contact):
    app.open_contact_home_page()
    app.go_to_new_contact_editor_page()

    # For purpose of exercise with only 4 selected parameters, adding 'personal data' is enough
    app.contact_data.enter_contact_personal_data(new_contact)

    app.contact_data.finalize_new_contact_addition()


@when(parsers.parse('a new <firstname>, <middlename>, <lastname> and <nickname> is entered'), target_fixture='modify_contact_data')
def modify_contact_data(app, index, firstname, middlename, lastname, nickname):

    old_contacts = app.contact_data.get_contact_list()

    # Edit the contact data

    con = Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname)

    con.id = old_contacts[index].id

    app.contact_data.modify_initialize(index)
    # For purpose of exercise with only 4 selected parameters, adding 'personal data' is enough
    app.contact_data.enter_contact_personal_data(con)

    app.contact_data.finalize_new_contact_addition()


@when('I delete the contact from the list')
def delete_contact(app, index):
    app.contact_data.delete_contact_by_index(index)


@then('the new contact list is equal to old contact list with modified contact')
def verify_contact_modified(app, non_empty_contact_list, index):

    old_contacts = non_empty_contact_list
    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts)

    old_contacts[index] = new_contacts[index]

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)


@then('new contact list is equal to the old contact list with new contact')
def verify_contact_added(app, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = app.contact_data.get_contact_list()
    old_contacts.append(new_contact)

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=id_or_max) == sorted(new_contacts, key=id_or_max)


@then('the new contact list is equal to old contact list without the deleted contact')
def verify_contact_deletion(app, non_empty_contact_list, index):

    old_contacts = non_empty_contact_list
    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts) - 1

    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted (new_contacts, key=Contact.id_or_max)

