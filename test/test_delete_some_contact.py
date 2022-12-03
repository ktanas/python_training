from random import randrange


def test_delete_some_contact(app):

    old_contacts = app.contact_data.get_contact_list()

    if app.contact_data.count() == 0:
        # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
        app.open_contact_home_page()
        app.go_to_new_contact_editor_page()
        app.contact_data.finalize_new_contact_addition()
        app.contact_data.return_to_home_page()

    app.open_contact_home_page()

    index = randrange(len(old_contacts))

    # app.contact_data.delete_first_contact()
    app.contact_data.delete_contact_by_index(index)

    app.open_contact_home_page()

    new_contacts = app.contact_data.get_contact_list()

    assert len(new_contacts) == len(old_contacts) - 1

    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

