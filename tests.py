import pytest
import main


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def list2():
    return [2, 3, 4, 5, 6]


def test_init(list1, list2):
    """Проверка корректной инициализации класса"""
    nums_list = main.Lists(list1, list2)
    assert nums_list.list1 == list1
    assert nums_list.list2 == list2


def test_first_average_more(list1, list2, capfd):
    nums_list = main.Lists(list2, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'avg list 1 > avg list 2'


def test_second_average_more(list1, list2, capfd):
    nums_list = main.Lists(list1, list2)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'avg list 1 < avg list 2'


def test_equal_averages(list1, capfd):
    nums_list = main.Lists(list1, list1)
    nums_list.compare_averages()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'avg list 1 = avg list 2'


def test_get_lists_averages(list1, list2):
    """Проверка средних значений списков размером больше 1"""
    nums_list = main.Lists(list1, list2)
    assert nums_list.get_lists_averages() == (3, 4)
