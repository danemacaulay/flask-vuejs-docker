#!/usr/bin/env python
import pytest

from services import run_app

print(__name__)

@pytest.fixture
def app():
    app_ = run_app()
    return app_