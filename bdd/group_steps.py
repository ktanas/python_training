from model.group import Group
from sys import maxsize
from random import randrange
from pytest_bdd import given, when, then, parsers


@given(parsers.parse('a group with {group_name}, {header_name} and {footer_name}'), target_fixture='new_group')
def new_group(group_name, header_name, footer_name):
    return Group(group_name=group_name, header_name=header_name, footer_name=footer_name)


@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()


@given('a non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="", header_name="", footer_name=""))
        return db.get_group_list()


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@when(parsers.parse('I modify {name}, {header} and {footer} of the chosen group'), target_fixture='modify_group_data')
def modify_group_data(app, index, new_name, new_header, new_footer):

    old_groups = app.group.get_group_list()

    group1 = Group(group_name=new_name, header_name=new_header, footer_name=new_footer)
    group1.id = old_groups[index].id

    app.group.modify_group_by_index(index, group1)

    return app.group.get_group_list()


@then('the new group list is equal to old group list with modified group')
def verify_group_modified(app, non_empty_group_list, index):
    old_groups = non_empty_group_list
    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[index] = new_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="", header_name="", footer_name=""))
        return db.get_group_list()

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize
    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)

@given('index of a random group from the list')
def random_group(non_empty_group_list):
    return randrange(len(non_empty_group_list))

@when('I delete the group from the list')
def delete_group(app, index):
    app.group.delete_group_by_index(index)

@then('the new group list is equal to old group list without the deleted group')
def verify_group_deletion(app, non_empty_group_list, index):
    old_groups = non_empty_group_list
    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups) - 1
    old_groups[index:index+1] = []
    assert old_groups == new_groups

