import pytest
import types
from src.curring import curry


def test_type():
    def foo():
        return 1

    assert isinstance(curry(foo), types.FunctionType)


def test_sum():
    def mysum(a, b, c):
        return a + b + c

    f = curry(mysum)
    assert f(1)(2)(3) == 6
    assert f(1, 3, 4) == 8
    assert f(1)(2, 6) == 9


def test_multiple_funcs():
    def foo1():
        return 1

    def foo2():
        return 2

    def foo3():
        return 3

    f1 = curry(foo1)
    f2 = curry(foo2)
    f3 = curry(foo3)

    assert f2() == 2
    assert f3() == 3
    assert f1() == 1


def megasum(a, *args):
    """Helper function for following tests"""
    for val in args:
        a += val
    return a


@pytest.mark.parametrize(
    ["args", "expected"],
    [
        ([(1), (2), (3), (4), (5)], 15),
        ([("bober"), ("ananas"), ("maxim")], "boberananasmaxim"),
    ],
)
def test_variadic_args(args, expected):
    def megasum(a, *args):
        for val in args:
            a += val
        return a

    result = curry(megasum, len(args))
    for arg in args:
        result = result(arg)
    assert result == expected


def test_argcount():
    f = curry(megasum, 3)
    f = f("12")("34")
    assert isinstance(f, types.FunctionType)

    f = f("56")
    assert f == "123456"
