import os
import requests
import pytest
from unittest import mock

class App:

    def get_json(self):
        return requests.get("https://www.baidu.com").json()


app = App()


class MockResponse:

    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)


@pytest.mark.usefixtures("mock_response")
def test_get_json():
    result = app.get_json()
    assert result["mock_key"] == "mock_response"


def get_os_user_lower():
    username = os.getenv("USER")
    if username is None:
        raise OSError("USER environment is not set.")
    return username.lower()


def test_username(monkeypatch):
    monkeypatch.setenv("USER", "A")
    assert get_os_user_lower() == "a"


def test_raise_exception(monkeypatch):
    monkeypatch.delenv("USER", raising=False)
    with pytest.raises(OSError):
        get_os_user_lower()


d = {"k": "v", "a": "a1"}
print(id(d))

@pytest.fixture
def mock_setitem(monkeypatch):
    monkeypatch.setitem(d, "a", 1)

@pytest.fixture
def mock_delitem(monkeypatch):
    monkeypatch.delitem(d, "a")


def test_setitem(mock_setitem):
    assert d == {"k": "v", "a": 1}


def test_delitem(mock_delitem):
    print(id(d))
    assert d == {"k": "v"}


def print_session():
    from flask import session
    print(session.sid)


def test_patch():
    from flask import Flask
    flask_app = Flask(__name__)
    with flask_app.test_request_context():
        with mock.patch("flask.session") as mock_session:
            mock_session.sid = "mock_sid"
            print_session()