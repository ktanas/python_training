from model.group import Group
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o =="-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(group_name="", header_name="", footer_name="")] + [
    Group(group_name=random_string("", 15), header_name=random_string("", 15), footer_name=random_string("", 15))
    for i in range(n)
]
    # this comment should remain for teaching purposes, it is another way of defining test data
    #[Group(group_name="", header_name="", footer_name="")] + [
    #Group(group_name=random_string("group_name", 10),
    #      header_name=random_string("header_name", 20),
    #      footer_name=random_string("footer_name", 20))

    # Group(group_name=group_name, header_name=header_name, footer_name=footer_name)
    # for group_name in ["", random_string("group_name", 10)]
    # for header_name in ["", random_string("header_name", 20)]
    # for footer_name in ["", random_string("footer_name", 20)]
# ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as outFile:
    jsonpickle.set_encoder_options("json", indent=2)
    outFile.write(jsonpickle.encode(testdata))
