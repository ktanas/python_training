from model.group import Group
from random import randrange
import pytest

def test_modify_group_name(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name=""))

    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))

    group1 = Group(group_name="New group")
    group1.id = old_groups[index].id

    app.group.modify_group_by_index(index, group1)

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[index] = group1 # new_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):

    if app.group.count() == 0:
        app.group.create(Group(header_name=""))

    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))

    group1 = Group(header_name="YYYYYYYY")
    group1.id = old_groups[index].id

    app.group.modify_group_by_index(index, group1)

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[index] = new_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):

    if app.group.count() == 0:
        app.group.create(Group(footer_name=""))

    old_groups = app.group.get_group_list()

    index = randrange(len(old_groups))

    group1 = Group(footer_name="ZZZZZZZ")
    group1.id = old_groups[index].id

    app.group.modify_group_by_index(index, group1)

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[index] = new_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    old_groups = app.group.get_group_list()

    group1 = Group(group_name="A", header_name="B", footer_name="C")
    group1.id = old_groups[0].id

    # Change data of first group in the group list
    # new name: A, new header: B, new footer: C
    app.group.modify_first_group(group1)

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[0] = group1 # new_groups[0]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group(app, group_name, header_name, footer_name):

    with pytest.allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

        old_groups = app.group.get_group_list()

    with pytest.allure.step('Given index of a random group from the list'):
        index = randrange(len(old_groups))

    with pytest.allure.step('When I modify <%s>, <%s> and <%s> of the chosen group' % group_name % header_name % footer_name):
        group1 = Group(group_name=group_name, header_name=header_name, footer_name=footer_name)
        group1.id = old_groups[index].id

        app.group.modify_group_by_index(index, group1)

    with pytest.allure.step('Then the new group list is equal to old group list with modified group'):
        new_groups = app.group.get_group_list()

        assert len(new_groups) == len(old_groups)
        old_groups[index] = new_groups[index]
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
