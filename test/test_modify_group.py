from model.group import Group


def test_modify_group_name(app):

    app.group.modify_first_group(Group(group_name="XXXXXX"))


def test_modify_group_header(app):

    app.group.modify_first_group(Group(header_name="YYYYYYYY"))


def test_modify_group_footer(app):

    app.group.modify_first_group(Group(footer_name="ZZZZZZZ"))


def test_modify_first_group(app):

    # Change data of first group in the group list
    # new name: A, new header: B, new footer: C
    app.group.modify_first_group(Group(group_name="A", header_name="B", footer_name="C"))
