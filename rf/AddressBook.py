from fixture import application
from fixture.db import DbFixture
import json
import os.path
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'

    def __init__(self, config="target.json", browser="firefox"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as conf:
            self.target = json.load(conf)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = application.Application(browser=self.browser, base_url=web_config["base_url"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                                   user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        self.fixture.tear_down()
        self.dbfixture.destroy()

    def new_group(self, group_name, header_name, footer_name):
        return Group(group_name=group_name, header_name=header_name, footer_name=footer_name)

    def get_group_list(self):
        return self.fixture.group.get_group_list()

    def make_sure_that_group_list_is_not_empty(self):
        if self.fixture.group.count() == 0:
            self.fixture.group.create(Group(group_name="A", header_name="B", footer_name="C"))

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def enter_new_group_data(self, index, group):
        #group1 = Group(group_name=group.group_name, header_name=group.header_name, footer_name=group.footer_name)
        #group1.id = group.id

        self.fixture.group.modify_group_by_index(index, group)

    #def append_to_list(self, list, group):
    #    list.append(group)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def get_contact_list(self):
        return self.fixture.contact_data.get_contact_list()

    def new_contact(self, firstname, middlename, lastname, nickname):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname)

    def create_contact(self, contact):
        # This delay is necessary to give the application enough time to load.
        # Without this delay, this particular test fails, because the 'home' button on the upper toolbar of the
        # 'Addressbook' page is not visible when 'app.open_contact_home_page()' function is performed.
        self.fixture.delay(1)

        self.fixture.open_contact_home_page()
        self.fixture.go_to_new_contact_editor_page()
        self.fixture.contact_data.enter_contact_personal_data(contact)
        self.fixture.contact_data.finalize_new_contact_addition()

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def make_sure_that_contact_list_is_not_empty(self):
        if self.fixture.contact_data.count() == 0:
            # If list of contacts is empty, let us execute the set of methods used to create a new, empty contact
            self.fixture.open_contact_home_page()
            self.fixture.go_to_new_contact_editor_page()
            self.fixture.contact_data.finalize_new_contact_addition()
            self.fixture.contact_data.return_to_home_page()

    def enter_new_contact_data(self, index, contact):
        #con = Contact(firstname=contact.firstname, middlename=contact.middlename,
        #              lastname=contact.lastname, nickname=contact.nickname)
        #con.id = contact.id

        self.fixture.contact_data.modify_initialize(index)
        self.fixture.contact_data.enter_contact_personal_data(contact)
        self.fixture.contact_data.modify_finalize()

    def delete_contact(self, index):
        self.fixture.contact_data.delete_contact_by_index(index)
        self.fixture.open_contact_home_page()
