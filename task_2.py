"""
Функция, которая принимает список из чисел и возвращает их сумму.
Если в списке присутствуют не валидные данные, то возвращается индекс не валидных элементов в списке
"""
def sum_numbers(data):
    invalid_indices = []
    total_sum = 0

    def validate_and_sum(value, index_path):
        nonlocal total_sum
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            total_sum += value
        elif isinstance(value, list) or isinstance(value, tuple):
            for i, elem in enumerate(value):
                validate_and_sum(elem, index_path + [i])
        else:
            invalid_indices.append(index_path)

    for i, item in enumerate(data):
        validate_and_sum(item, [i])

    return total_sum if not invalid_indices else invalid_indices

lists = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5.1],
    [1, 2, 3, 4, 5.0],
    [1, 2, 3, [4, 5.0]],
    [1, 2, "three", 4, 5.0],
    [1, 2, ["three", 4, 5.0]],
    [True, 2, ("three", [{}, 5.0])]
]

for list_ in lists:
    print(sum_numbers(list_))
