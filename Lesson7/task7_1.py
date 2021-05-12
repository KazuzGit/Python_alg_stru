"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.

"""
import random

SIZE = 10
array = [random.randint(-100, 99) for i in range(SIZE)]


def bubble_sort(arr, last):
    while last != 0:
        i = 0
        while i < last:
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
        last -= 1


print(array)
bubble_sort(array, len(array) - 1)
print(array)
