from model.group import Group
from random import randrange
import pytest


def test_delete_group(app):

    # Additional test made for purpose of Allure framework testing

    with pytest.allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

        old_groups = app.group.get_group_list()

    with pytest.allure.step('Given index of a random group from the list'):
        index = randrange(len(old_groups))

    with pytest.allure.step('When I delete the group from the list'):
        app.group.delete_group_by_index(index)

    with pytest.allure.step('Then the new group list is equal to old group list without the deleted group'):
        new_groups = app.group.get_group_list()

        assert len(new_groups) == len(old_groups) - 1
        old_groups[index:index+1] = []
        assert old_groups == new_groups
