# 1. Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.
# исходник из task2_4

import timeit
import cProfile

def summ_range(cur, n):
    if (n == 1):
        return cur
    return cur + summ_range(cur * (-0.5), n - 1)

print(timeit.timeit('summ_range(1, 10)', number=1000, globals=globals()))   # 0.0008199999999999995
print(timeit.timeit('summ_range(1, 100)', number=1000, globals=globals()))  # 0.008875300000000001
print(timeit.timeit('summ_range(1, 992)', number=1000, globals=globals()))  # 0.1408987

cProfile.run('summ_range(1, 992)')
# 992/1    0.001    0.000    0.001    0.001 task4_1.py:4(summ_range)
# медленно выполнияется из-за рекурсии


def arr_range(n):
    arr = [1 / (-2) ** i for i in range(1, n)]
    summ_ = 1
    for i in arr:
        summ_ += i
    return summ_

print(timeit.timeit('arr_range(10)', number=1000, globals=globals()))   # 0.0020802000000001986
print(timeit.timeit('arr_range(100)', number=1000, globals=globals()))  # 0.03658159999999988
print(timeit.timeit('arr_range(992)', number=1000, globals=globals()))  # 0.7703335999999998

cProfile.run('arr_range(992)')
# 1    0.001    0.001    0.001    0.001 task4_1.py:29(<listcomp>)
# тратим время на создание списков

def summ_for(n):
    summ_ = 1
    a = 1
    for i in range(1, n):
        a /= -2
        summ_ += a
    return summ_

print(timeit.timeit('summ_for(10)', number=1000, globals=globals()))    # 0.0005779000000001311
print(timeit.timeit('summ_for(100)', number=1000, globals=globals()))   # 0.0043751999999999125
print(timeit.timeit('summ_for(992)', number=1000, globals=globals()))   # 0.04696239999999996

cProfile.run('summ_for(992)')
# 4 function calls in 0.000 seconds
#
#По результатам замеров 3 вариантов функций для N - 10, 100 и 992 можно сделать вывод:
# самое эффективное решение № 3;
# все 3 варианта работают в линейной прогрессии О(n).
#

