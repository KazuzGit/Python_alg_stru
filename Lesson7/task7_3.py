"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.

"""
import random


def partition(_array, low, high):
    point = _array[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while _array[i] < point:
            i += 1
        j -= 1
        while _array[j] > point:
            j -= 1

        if i >= j:
            return j
        _array[i], _array[j] = _array[j], _array[i]


def _sort(_array):

    def _quick_sort(items, low, high):
        if low < high:
            _split_index = partition(items, low, high)
            _quick_sort(items, low, _split_index)
            _quick_sort(items, _split_index + 1, high)

    _quick_sort(_array, 0, len(_array) - 1)


SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE * 2 + 1)]
print(f'Исходный массив: {_array}')
_sort(_array)
print(f'Отсортированный массив: {_array}')
print(f'Медиана: {_array[len(_array) // 2]}')
