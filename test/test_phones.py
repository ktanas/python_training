import re
from random import randrange


def test_phones_on_home_page(app):
    list_of_contacts = app.contact_data.get_contact_list()
    index = randrange(len(list_of_contacts))

    contact_from_home_page = list_of_contacts[index]
    contact_from_edit_page = app.contact_data.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

    #assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    #assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    #assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    #assert contact_from_home_page.extra_phone == clear(contact_from_edit_page.extra_phone)


def test_phones_on_contact_view_page(app):
    list_of_contacts = app.contact_data.get_contact_list()
    index = randrange(len(list_of_contacts))

    contact_from_view_page = app.contact_data.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact_data.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.extra_phone == contact_from_edit_page.extra_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.extra_phone]))))