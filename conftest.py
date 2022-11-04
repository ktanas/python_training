# -*- coding: utf-8 -*-
from fixture.application_group import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.tear_down)
    return fixture
