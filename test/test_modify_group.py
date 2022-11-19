from model.group import Group


def test_modify_group_name(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name=""))

    old_groups = app.group.get_group_list()

    group1 = Group(group_name="New group")
    group1.id = old_groups[0].id

    app.group.modify_first_group(group1)
    # app.group.modify_first_group(Group(group_name="XXXXXX"))

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[0] = group1
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):

    if app.group.count() == 0:
        app.group.create(Group(header_name=""))

    old_groups = app.group.get_group_list()

    app.group.modify_first_group(Group(header_name="YYYYYYYY"))

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)

def test_modify_group_footer(app):

    if app.group.count() == 0:
        app.group.create(Group(footer_name=""))

    old_groups = app.group.get_group_list()

    app.group.modify_first_group(Group(footer_name="ZZZZZZZ"))

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)

def test_modify_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    old_groups = app.group.get_group_list()

    # Change data of first group in the group list
    # new name: A, new header: B, new footer: C
    app.group.modify_first_group(Group(group_name="A", header_name="B", footer_name="C"))

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
