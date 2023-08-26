from app.logic import calc


def test_add():
    assert calc.add(8, 3) == 11
