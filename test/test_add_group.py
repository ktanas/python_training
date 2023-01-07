# -*- coding: utf-8 -*-
from sys import maxsize


def test_add_group(app, db, json_groups):

    group = json_groups

    old_groups = db.get_group_list()

    # Create a new group
    app.group.create(group)

    # assert app.group.count() == len(old_groups) + 1
    new_groups = db.get_group_list()

    old_groups.append(group)

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize

    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)
