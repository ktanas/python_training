def number_of_filled_rows_in_excel_sheet(sheet):
    # Compute number of filled rows in a given Microsoft Excel sheet.
    # This function is used to determine number of groups/contacts listed in
    # an Excel sheet when loading data from there.
    # This function knows the format in which these files are generated,
    # so we can assume that there are no empty rows in the beginning of the sheet
    # or between the filled rows.

    i = 1
    stop = False

    while stop==False:
        # print(sheet["A%s" % i].value + "XXX\n")
        if sheet["A%s" % i].value is None:
            stop = True
        else:
            i=i+1

    return i-1





