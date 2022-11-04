# -*- coding: utf-8 -*-

def test_modify_first_group(app):
    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    # Change data of first group in the group list
    # new name: Group2, new header: Header2, new footer: Footer2
    app.group.modify_initialize()
    app.group.modify_group_name("Group2")
    app.group.modify_group_header("Header2")
    app.group.modify_group_footer("Footer2")
    app.group.modify_finalize()

    app.group.return_to_group_page()

    app.session.logout()