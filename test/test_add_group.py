# -*- coding: utf-8 -*-
from model.group import Group
from sys import maxsize


def test_add_group(app):

    old_groups = app.group.get_group_list()

    group1 = Group(group_name="Group1", header_name="Header1", footer_name="Footer1")

    # Create a new group
    app.group.create(group1)

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups) + 1

    old_groups.append(group1)

    # def id_or_max(gr):
    #    if gr.id:
    #        return int(gr.id)
    #    else:
    #        return maxsize

    # assert (old_groups == new_groups)
    # assert (sorted(old_groups) == sorted(new_groups))
    # assert sorted (old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)

    assert sorted(old_groups, key=Group.id_or_max) == sorted (new_groups, key=Group.id_or_max)