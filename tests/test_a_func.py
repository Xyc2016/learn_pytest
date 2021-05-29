import pytest


def add_one(x):
    return x + 1


def test_answer():
    # assert 1 == 2
    pass

def f_that_raise():
    raise ValueError("?????")


def test_f_raise():
    with pytest.raises(ValueError) as e:
        f_that_raise()

    print(e.traceback)













