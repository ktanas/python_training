from model.contact import *
from utilities import contact_utilities

birth_data = contact_utilities.generate_random_valid_day()
anniversary_data = contact_utilities.generate_random_valid_day()

testdata = [
    Contact(
        firstname=contact_utilities.random_string(15),
        middlename=contact_utilities.random_string(10),
        lastname=contact_utilities.random_string(15),
        nickname=contact_utilities.random_string(20),
        photo_file_location="C:\\users\\ktana\\PyCharmProjects\\python_training\\aircraft_engine.JPG",
        title="Senior Production Engineer",
        company="J&S Machinery Inc.",
        address="123 White Street\n00-123 Chicago, Illinois\nUnited States",
        home_phone=contact_utilities.random_digits(9),
        mobile_phone=contact_utilities.random_digits(9),
        work_phone=contact_utilities.random_digits(9),
        fax=contact_utilities.random_digits(10),
        email="jsmith@jsmachinery.com",
        email2="xxx@yyy.zzz.com",
        email3="abc123@abc.com",
        home_page="https://www.jsmachinery.com/~jsmith",
        birth_day=birth_data[0],
        birth_month=birth_data[1],
        birth_year=birth_data[2],
        anniversary_day=anniversary_data[0],
        anniversary_month=anniversary_data[1],
        anniversary_year=anniversary_data[2],
        group_name="[none]",
        extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
        extra_phone=contact_utilities.random_digits(9),
        notes="A nice record to test in Python!"
        # ,id=id
    ),
    Contact(
        firstname="Anne",
        lastname="Jones",
        birth_day="31",
        birth_month="December",
        birth_year="1999"
    )
]