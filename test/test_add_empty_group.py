# -*- coding: utf-8 -*-
from model.group import Group


def test_add_empty_group(app):

    old_groups = app.group.get_group_list()

    # Create an empty group
    app.group.create(Group(group_name="", header_name="", footer_name=""))

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups) + 1
