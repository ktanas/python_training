# -*- coding: utf-8 -*-
from fixture import application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")

    if fixture is None:
        fixture = application.Application(browser=browser, base_url=base_url,
                                          username=username, password=password)
    else:
        if not fixture.is_valid():
            fixture = application.Application(browser=browser, base_url=base_url,
                                              username=username, password=password)

    fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.tear_down()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--username", action="store", default="admin")
    parser.addoption("--password", action="store", default="secret")
