from pytest_bdd import given, when, then
from model.group import Group
from sys import maxsize
from random import randrange


@given('a group list')
def group_list(db):
    return db.get_group_list()


@given('a group with <group_name>, <header_name> and <footer_name>')
def new_group(group_name, header_name, footer_name):
    return Group(group_name=group_name, header_name=header_name, footer_name=footer_name)


#@given('a group with name1, header1 and footer1')
#def new_group():
#    return Group(group_name="name1", header_name="header1", footer_name="footer1")


#@given('a group with name2, header2 and footer2')
#def new_group():
#    return Group(group_name="name2", header_name="header2", footer_name="footer2")


#@when('I add a new group with <name>, <header> and <footer>')
#def add_new_group(app, name, header, footer):
#    app.group.create(Group(group_name=name, header_name=header, footer_name=footer))

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="", header_name="", footer_name=""))
        return db.get_group_list()

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list()
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

