from model.group import Group


testdata = [
    Group(group_name="group1", header_name="header1", footer_name="footer1"),
    Group(group_name="group2", header_name="header2", footer_name="footer2")
]


#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [
    # this comment should remain for teaching purposes, it is another way of defining test data
    #[Group(group_name="", header_name="", footer_name="")] + [
    #Group(group_name=random_string("group_name", 10),
    #      header_name=random_string("header_name", 20),
    #      footer_name=random_string("footer_name", 20))

#    Group(group_name=group_name, header_name=header_name, footer_name=footer_name)
#    for group_name in ["", random_string("group_name", 10)]
#    for header_name in ["", random_string("header_name", 20)]
#    for footer_name in ["", random_string("footer_name", 20)]
#]
