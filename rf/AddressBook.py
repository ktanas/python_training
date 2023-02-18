from fixture import application
from fixture.db import DbFixture
import json
import os.path
from model.group import Group


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

    def create_group(self, name, header, footer):
        self.fixture.group.create(Group(group_name=name, header_name=header, footer_name=footer))

