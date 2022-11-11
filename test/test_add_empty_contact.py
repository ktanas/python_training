from model.contact import *


def test_add_empty_contact(app):

    con = Contact(firstname="",
                  middlename="",
                  lastname="",
                  nickname="",
                  photo_file_location="",
                  title="",
                  company="",
                  address="",
                  home_phone="",
                  mobile_phone="",
                  work_phone="",
                  fax="",
                  email="",
                  email2="",
                  email3="",
                  home_page="",
                  birth_day="",
                  birth_month="",
                  birth_year="",
                  anniversary_day="",
                  anniversary_month="",
                  anniversary_year="",
                  group_name="",
                  extra_address="",
                  extra_phone="",
                  notes="")

    app.open_contact_home_page()

    app.go_to_new_contact_editor_page()

    app.contact_data.finalize_new_contact_addition()

    app.contact_data.return_to_home_page()
