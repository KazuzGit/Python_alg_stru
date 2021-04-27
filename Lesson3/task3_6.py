""""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.

"""

from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_index = 0
max_index = 0

for i in range(len(array)):
    if array[i] < array[min_index]:
        min_index = i
    if array[i] > array[max_index]:
        max_index = i

print(min_index, max_index)

sum_ = 0

if min_index < max_index:
    for i in range(min_index + 1, max_index):
        sum_ += array[i]
else:
    for i in range(max_index + 1, min_index):
        sum_ += array[i]

print(f'Сумма элементов массива, находящихся между минимальным и максимальным = {sum_}')