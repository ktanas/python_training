# -*- coding: utf-8 -*-
from fixture import application
import pytest

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = application.Application()
    else:
        if not fixture.is_valid():
            fixture = application.Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.tear_down()
    request.addfinalizer(fin)
    return fixture
