from model.group import Group
from random import randrange


def test_delete_some_group(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    print("len(old_groups)="+str(len(old_groups)))
    print("index="+str(index))

    app.group.delete_group_by_index(index)

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups) - 1
    old_groups[index:index+1] = []
    assert old_groups == new_groups
