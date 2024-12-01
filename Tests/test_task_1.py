import pytest

from task_1 import print_int


@pytest.mark.parametrize(
    'start_range, end_range, div1, div2, expected',
    (
        (1, 5, 3, 5, '1\n2\nFizz\n4\nBuzz\n'),
        (1, 5, 1, 1, 'FizzBuzz\nFizzBuzz\nFizzBuzz\nFizzBuzz\nFizzBuzz\n'),
        (15, 15, 5, 10, 'Fizz\n')
    )
)
def test_print_int(capsys, start_range, end_range, div1, div2, expected):
    #Тестирование задания 1
    print_int(start_range, end_range, div1, div2)
    captured = capsys.readouterr()
    assert captured.out == expected
