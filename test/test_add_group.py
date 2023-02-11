# -*- coding: utf-8 -*-
from sys import maxsize
import pytest


def test_add_group(app, db, json_groups):

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize

    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()

    with pytest.allure.step('When I add a group %s to the list' % group):
        # Create a new group
        app.group.create(group)

    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        # assert app.group.count() == len(old_groups) + 1
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)
