import sys
import pytest
import app

@pytest.mark.smoke
def test_smoke_add():
    assert app.add(1, 1) == 2

@pytest.mark.parametrize("value", ["1", "22", "65535"])
def test_parse_port_ok(value):
    assert app.parse_port(value) == int(value)

@pytest.mark.parametrize("value", ["0", "65536", "-1"])
def test_parse_port_out_of_range(value):
    with pytest.raises(ValueError, match="out of range"):
        app.parse_port(value)

@pytest.mark.skipif(sys.platform.startswith("win"), reason="demo skip")
def test_skipif_demo():
    assert True

@pytest.mark.xfail(reason="known bug")
def test_xfail_demo_for_known_bug():
    assert app.normalize_name(" Alice ") == "alice"

@pytest.mark.slow
def test_slow_demo():
    assert True
