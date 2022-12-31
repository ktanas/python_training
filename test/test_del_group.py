from model.group import Group


def test_delete_first_group(app, db):

    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    old_groups = db.get_group_list()
    # group = random.choice(old_groups)

    app.group.delete_first_group()
    # app.group.delete_group_by_id(group.id)

    new_groups = db.get_group_list()

    assert len(new_groups) == len(old_groups) - 1
    old_groups[0:1] = []
    # old_groups.remove(group)
    assert old_groups == new_groups
