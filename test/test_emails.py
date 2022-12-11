import re
from random import randrange


def test_emails_on_home_page(app):
    list_of_contacts = app.contact_data.get_contact_list()
    index = randrange(len(list_of_contacts))

    contact_from_home_page = list_of_contacts[index]
    contact_from_edit_page = app.contact_data.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_emails_on_contact_view_page(app):
    list_of_contacts = app.contact_data.get_contact_list()
    index = randrange(len(list_of_contacts))

    contact_from_view_page = app.contact_data.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact_data.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.email == contact_from_edit_page.email
    assert contact_from_view_page.email2 == contact_from_edit_page.email2
    assert contact_from_view_page.email3 == contact_from_edit_page.email3


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))