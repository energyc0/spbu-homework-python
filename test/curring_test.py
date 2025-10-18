import pytest
import types
from src.curring import curry, uncurry


def foo():
    """Helper function for following tests."""
    return 1


def megasum(a, *args):
    """Helper function for following tests."""
    for val in args:
        a += val
    return a


def test_type_curry():
    assert isinstance(curry(foo, 0), types.FunctionType)


def test_type_uncurry():
    f = curry(foo, 0)
    assert isinstance(uncurry(f, 0), types.FunctionType)


def test_sum():
    def mysum(a, b, c):
        return a + b + c

    f = curry(mysum, 3)
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

    f1 = curry(foo1, 0)
    f2 = curry(foo2, 0)
    f3 = curry(foo3, 0)

    assert f2() == 2
    assert f3() == 3
    assert f1() == 1


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

    def myfoo():
        return 1234

    with pytest.raises(Exception):
        curry(myfoo, 1)
    with pytest.raises(Exception):
        curry(myfoo, -1)
    with pytest.raises(Exception):
        curry(megasum, 0)


def test_uncurried():
    f = curry(megasum, 4)
    f = uncurry(f, 4)
    assert f(1, 2, 3, 4) == 1 + 2 + 3 + 4

    with pytest.raises(TypeError):
        f(1, 2)
