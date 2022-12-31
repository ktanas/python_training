import pymysql.cursors
from fixture.orm import ORMFixture
# from fixture.db import DbFixture

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))

    # l = db.get_group_list()
    # for item in l:
    #    print(item)
    # print(len(l))

    # contacts = db.get_contact_list()
    # for contact in contacts:
    #     print(contact)
    # print(len(contacts))

    # groups = db.get_group_list()
    # for group in groups:
    #    print(group)
    # print(len(groups))

    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM group_list")
    # for row in cursor.fetchall():
    #    print(row)

finally:
    pass
    # connection.close()
    # db.destroy()
