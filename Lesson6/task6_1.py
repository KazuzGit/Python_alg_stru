"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

task2_2 Посчитать четные и нечетные цифры введенного натурального числа.

"""
import sys
from collections import deque


def sum_(object):
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
               sum_(key)
               sum_(value)
        elif not isinstance(object, str):
            for item in object:
                sum_(item)
    array.append(sys.getsizeof(object))
    result = sum(array) - 120  # 120 - выбросим на список для этой функции

    return result

# Исходный вариант
def var_1(numb):
    array_2 = []
    numb_2 = numb
    a = 0  # четные
    b = 0  # нечетные

    while numb_2 > 0:
        if numb_2 % 2 == 0:
            a += 1
        else:
            b += 1
        numb_2 = numb_2 // 10

    array_2.extend([a, b, numb, numb_2])

    return f'В числе {numb} находится {a} четных цифр и {b} нечетных. Выделено памяти {(sum_(array_2))}'


def var_2(numb):
    array_3 = []
    a, b = 0, 0
    for i in numb:
        if i in {'0', '2', '4', '6', '8'}:
            a += 1
        else:
            b += 1

    array_3.extend([a, b, numb])

    return f'В числе {numb} находится {a} четных цифр и {b} нечетных. Выделено памяти {(sum_(array_3))}'


def var_3(numb):
    array_4 = []
    array = []
    a, b = 0, 0

    for i in numb:
        i = int(i)
        array.append(i)

    for i in array:
        if i % 2 == 0:
            a += 1
        else:
            b += 1

    array_4.extend([numb, a, b, array, i])

    return f'В числе {numb} находится {a} четных цифр и {b} нечетных. Выделено памяти {sum_(array_4)}'

array = []
numb_us = int(input('Введите натуральное число: '))

print(var_1(numb_us))

array = []
numb_us_2 = input('Введите натуральное число: ')


print(var_2(numb_us_2))

array = []
numb_us_3 = deque(input('Введите натуральное число: '))


print(var_3(numb_us_3))


"""
Для натурального числа: 12345678901234567890
1 вариант: выделено памяти 116 байт
2 вариант: выделено памяти 125 байт
3 вариант: выделено памяти 2,44 Кбайт

Наиболее оптимальный вариант по результатам тестов №1,
с типом переменной int, есть варианты, когда второй вариант (str), показывает результаты чуть лучше,
при числах 10, 11 и т.п., но это из-за не совершенного моего варианта,
если немного оптимизировать и убрать переменную numb_2,
первый вариант будет всегда выигрышней по памяти.

Windows 10 Pro, версия 20H2, 64-разрядная операционная система, процессор x64
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32

"""