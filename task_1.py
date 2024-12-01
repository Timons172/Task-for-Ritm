"""
Функция, которая выводит числа в заданном диапазоне.
При этом, если число кратно одному из двух делителей, то выводится 'Fizz' или 'Buzz' соответственно.
При этом, если число кратно двум делителям, то выводится 'FizzBuzz'.
"""
def print_int (*args):
    start, end, div1, div2 = args
    for i in range(start, end + 1):
        output = ""
        if i % div1 == 0:
            output += "Fizz"
        if i % div2 == 0:
            output += "Buzz"
        if not output:
            output = i
        print(output)

print_int(1, 35, 3, 5)
