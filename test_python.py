"""

В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt,
 pow, hypot. Чем больше тестов на каждую функцию - тем лучше

"""
import math

def test_filter():
    assert list(filter(lambda x: x[1] in 'abcd', ['adc', 'cbd', 'dbc', 'fgh'])) == ['adc', 'cbd', 'dbc'], 'test  error'
    assert list(filter(None, [-2, -1, 0, 1, 2])) == [-2, -1, 1, 2], 'test filter error'

def test_map():
    assert list(map(lambda x: x+1, [1, 2, 3])) == [2, 3, 4], 'test map error'
    assert list(map(lambda x: x-1, [1, 2, 3])) == [0, 1, 2], 'test map error'

def test_sorted():
    assert sorted([3, 2, 1]) == [1, 2, 3], 'test sorted error'
    assert sorted([5, 4, 3]) == [3, 4, 5], 'test sorted error'

def test_math_pi():
    assert int(math.pi) == 3, 'test pi error'
    assert round(math.pi, 3) == 3.141, 'test pi error'


def test_math_sqrt():
    assert math.sqrt(4) == 2, 'test sqrt error'
    assert math.sqrt(9) == 3, 'test sqrt error'


def test_math_pow():
    assert math.pow(0, 3) == 0, 'test pow error'
    assert math.pow(1, 3) == 1, 'test pow error'
    assert math.pow(2, 3) == 8, 'test pow error'
    assert math.pow(3, 3) == 27, 'test pow error'


def test_math_hypot():
    assert math.hypot(0, 0) == 0, 'Test failed!!!'
    assert round(math.hypot(1, 1), 2) == 1.41, 'Test failed!!!'
    assert round(math.hypot(2, 2), 2) == 2.82, 'Test failed!!!'








