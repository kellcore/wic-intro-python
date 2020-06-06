def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(5, 4) == 1


def test_divide():
    assert divide(10, 5) == 2
