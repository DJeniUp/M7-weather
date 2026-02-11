def test_assert_introspection():
    x = y = 0
    assert x != 2
    assert not x
    assert x < 3 or y > 5
