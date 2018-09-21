import pytest
from flask import url_for

def test_healthcheck_response(client):
    res = client.get(url_for('health_check'))
    assert res.status_code == 200
    assert res.data == b'{"msg": "Hello World"}'
