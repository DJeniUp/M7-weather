import pytest
from unittest.mock import Mock
import app

@pytest.mark.parametrize("bad", ["abc", "", "   "])
def test_parse_port_non_int_raises(bad):
    with pytest.raises(ValueError):
        app.parse_port(bad)

def test_greet_user_with_mock():
    gateway = Mock()
    gateway.get_user.return_value = {"name": "ALICE"}
    assert app.greet_user(1, gateway) == "Hello, alice!"
    gateway.get_user.assert_called_once_with(1)

class FakeGateway:
    def __init__(self, users):
        self.users = users
        self.calls = []

    def get_user(self, user_id: int) -> dict:
        self.calls.append(user_id)
        return self.users[user_id]

def test_greet_user_with_fake_gateway():
    fake = FakeGateway({7: {"name": "Bob"}})
    assert app.greet_user(7, fake) == "Hello, bob!"
    assert fake.calls == [7]

def test_monkeypatch_time(monkeypatch):
    monkeypatch.setattr(app, "get_current_timestamp", lambda: 123.0)
    assert app.get_current_timestamp() == 123.0
