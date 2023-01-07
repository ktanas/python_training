from model.group import Group
import random
import openpyxl
import os.path

from utilities.excel_utilities import number_of_filled_rows_in_excel_sheet

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def test_write_group_to_excel(app):

    if app.group.count() == 0:
        app.group.create(Group(group_name="", header_name="", footer_name=""))

    old_groups = app.group.get_group_list()

    index = random.randrange(len(old_groups))

    group = app.group.read_group_by_index(index)

    wb = openpyxl.load_workbook(os.path.join(project_dir, "groups2.xlsx"))
    # The Excel file name on which test is operating can be defined as a variable,
    # but let us assume that we use the same file (groups2.xlsx) for our tests
    sh = wb.active

    row_number_to_write = number_of_filled_rows_in_excel_sheet(sh) + 1

    sh["A%s" % row_number_to_write].value = group.group_name
    sh["B%s" % row_number_to_write].value = group.header_name
    sh["C%s" % row_number_to_write].value = group.footer_name

    new_groups = app.group.get_group_list()

    assert len(new_groups) == len(old_groups)
    old_groups[index] = new_groups[index]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
