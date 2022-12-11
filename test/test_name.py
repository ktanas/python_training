from random import randrange


def test_full_name(app):
    list_of_contacts = app.contact_data.get_contact_list()
    index = randrange(len(list_of_contacts))

    # print("test_full_name: index=", index)

    contact_from_view_page = app.contact_data.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact_data.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    assert contact_from_view_page.middlename == contact_from_edit_page.middlename
    assert contact_from_view_page.lastname == contact_from_edit_page.lastname
