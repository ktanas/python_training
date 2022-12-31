from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):

    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)

    # index = randrange(len(old_groups))
    # print("len(old_groups)="+str(len(old_groups)))
    # print("index="+str(index))

    # app.group.delete_group_by_index(index)
    app.group.delete_group_by_id(group.id)

    new_groups = db.get_group_list()

    assert len(new_groups) == len(old_groups) - 1
    # old_groups[index:index+1] = []
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
