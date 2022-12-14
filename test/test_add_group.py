# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string
from sys import maxsize


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    # this comment should remain for teaching purposes, it is another way of defining test data
    #[Group(group_name="", header_name="", footer_name="")] + [
    #Group(group_name=random_string("group_name", 10),
    #      header_name=random_string("header_name", 20),
    #      footer_name=random_string("footer_name", 20))

    Group(group_name=group_name, header_name=header_name, footer_name=footer_name)
    for group_name in ["", random_string("group_name", 10)]
    for header_name in ["", random_string("header_name", 20)]
    for footer_name in ["", random_string("footer_name", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    pass

    old_groups = app.group.get_group_list()

    # Create a new group
    app.group.create(group)

    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_group_list()

    old_groups.append(group)

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize

    # assert (old_groups == new_groups)
    # assert (sorted(old_groups) == sorted(new_groups))
    assert sorted(old_groups, key=id_or_max) == sorted(new_groups, key=id_or_max)

    # assert sorted(old_groups, key=Group.id_or_max) == sorted (new_groups, key=Group.id_or_max)
