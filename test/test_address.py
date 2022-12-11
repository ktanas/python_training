from random import randrange


def test_address_on_home_page(app):
    list_of_contacts = app.contact_data.get_contact_list()
    index = randrange(len(list_of_contacts))

    contact_from_home_page = list_of_contacts[index]
    contact_from_edit_page = app.contact_data.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address
