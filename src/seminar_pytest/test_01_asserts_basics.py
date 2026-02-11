import pytest
import app

def test_add_simple():
    assert app.add(2, 3) == 5

@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Alice", "alice"),
        ("ALICE", "alice"),
        (" Alice  ", "alice"),
        ("\tBob\n", "bob"),
    ],
)
def test_normalize_name(raw, expected):
    assert app.normalize_name(raw) == expected

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, True),
        (1, False),
        (2, True),
        (3, False),
        (10, True),
    ],
)
def test_is_even(n, expected):
    assert app.is_even(n) is expected
