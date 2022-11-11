# -*- coding: utf-8 -*-
from model.group import Group


def test_add_empty_group(app):

    # Create an empty group
    app.group.create(Group(group_name="", header_name="", footer_name=""))
