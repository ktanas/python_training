# -*- coding: utf-8 -*-
from fixture import application
import pytest


@pytest.fixture
def app(request):
    fixture = application.Application()
    request.addfinalizer(fixture.tear_down)
    return fixture
