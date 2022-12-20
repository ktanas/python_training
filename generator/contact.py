from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact
from utilities import contact_utilities

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


birth_data_list = []
for i in range(n):
    birth_data_list.append(contact_utilities.generate_random_valid_day())
anniv_data_list = []
for i in range(n):
    anniv_data_list.append(contact_utilities.generate_random_valid_day())

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
        birth_day=birth_data_list[i][0],
        birth_month=birth_data_list[i][1],
        birth_year=birth_data_list[i][2],
        anniversary_day=anniv_data_list[i][0],
        anniversary_month=anniv_data_list[i][1],
        anniversary_year=anniv_data_list[i][2],
        group_name="[none]",
        extra_address="66 Oak Avenue\n00-125 Chicago, Illinois\nUnited States",
        extra_phone=contact_utilities.random_digits(9),
        notes="A nice record to test in Python!"
        # ,id=id
    )
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as outFile:
    jsonpickle.set_encoder_options("json", indent=2)
    outFile.write(jsonpickle.encode(testdata))
