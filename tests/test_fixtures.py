import os
import shutil
import tempfile

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("Apple")


@pytest.fixture
def fruit_basket(my_fruit):
    print(f"{id(my_fruit)=}")
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket


@pytest.fixture
def first_entry():
    print("first_entry called")
    return "a"


@pytest.fixture
def order():
    print("order called")
    return []


@pytest.fixture
def append_fixture(order, first_entry):
    return order.append(first_entry)


def test_string_only(append_fixture, order, first_entry):
    assert order == [first_entry]


def test_conf(fixture_scope_module):
    # print(fixture_scope_module)
    pass


@pytest.fixture(params=[{"a": 1}, {"b": 1}, {"c": "c1"}])
def f_yield(request):
    print(f"{request.param}")
    d = {**request.param, "k": "v"}
    yield d
    print("finalizing d")


def test_yield(f_yield):
    print(f_yield)


@pytest.mark.usefixtures("cleandir")
class TestDirInit:
    def test_cwd_starts_empty(self):
        print(os.getcwd())
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")
        print(os.listdir(os.getcwd()))

