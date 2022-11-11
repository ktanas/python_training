from model.group import Group


def test_delete_first_group(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    app.group.delete_first_group()
