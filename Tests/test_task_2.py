import pytest

from task_2 import sum_numbers


@pytest.mark.parametrize(
    'list_, expected',
    (
        ([1, 2, 3, 4, 5], 15),
([1, 2, 3, 4, 5.1], 15.1),
([1, 2, 3, 4, 5.0], 15.0),
([1, 2, 3, [4, 5.0]], 15.0),
([1, 2, "three", 4, 5.0], [[2]]),
([1, 2, ["three", 4, 5.0]], [[2, 0]]),
([True, 2, ("three", [{}, 5.0])], [[0], [2, 0], [2, 1, 0]])
    )
)
def test_sum_numbers(list_, expected):
    #Тестирование задания 2
    assert sum_numbers(list_) == expected
