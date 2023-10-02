from utils import dicts


def test_get_val_1():
    assert dicts.get_val({}, "first") == "default"


def test_get_val_2():
    assert dicts.get_val({"first": 1}, "frst", "zero") == "zero"


def test_get_val_3():
    assert dicts.get_val({"first": 1, "second": 2}, "first", "zero") == 1


def test_get_val_4():
    assert dicts.get_val({"first": 1, "second": 2}, "second", "zero") == 2


def test_get_val_5():
    assert dicts.get_val({"first": 1, "second": 2}, "asd", "zero") == "zero"
