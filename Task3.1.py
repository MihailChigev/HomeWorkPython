# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2

# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1

list=[10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
print(list)
x=int(input())
a=(list.count(x))
print(f'цифра {x} повторяется в списке {a} раз(а)')
if x not in list:
    print('-1')

