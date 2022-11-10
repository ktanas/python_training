from model.group import Group


def test_modify_group_name(app):

    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    app.group.modify_first_group(Group(group_name="XXXXXX"))

    app.session.logout()


def test_modify_group_header(app):

    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    app.group.modify_first_group(Group(header_name="YYYYYYYY"))

    app.session.logout()


def test_modify_group_footer(app):

    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    app.group.modify_first_group(Group(footer_name="ZZZZZZZ"))

    app.session.logout()


def test_modify_first_group(app):
    # Login to 'Addressbook' as 'admin'
    app.session.login(username="admin", password="secret")

    # Change data of first group in the group list
    # new name: A, new header: B, new footer: C

    app.group.modify_first_group(Group(group_name="A", header_name="B", footer_name="C"))

    app.session.logout()
