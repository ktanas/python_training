# -*- coding: utf-8 -*-
from sys import maxsize
import openpyxl
import os.path
import random
from model.group import Group
from utilities.excel_utilities import number_of_filled_rows_in_excel_sheet

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def test_add_group_from_excel(app, db):

    old_groups = db.get_group_list()

    wb = openpyxl.load_workbook(os.path.join(project_dir, "groups2.xlsx"))
    sh = wb.active

    number_of_groups = number_of_filled_rows_in_excel_sheet(sh) - 1
    n = random.randrange(number_of_groups)

    group_name = sh["A%s" % (n+2)].value
    header_name = sh["B%s" % (n+2)].value
    footer_name = sh["C%s" % (n+2)].value

    group = Group(group_name=group_name, header_name=header_name, footer_name=footer_name)

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
