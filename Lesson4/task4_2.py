# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

import itertools
import timeit
import cProfile


def prime_num(a):
    counter = 0
    while counter < a:
        for i in itertools.count(2):

            for j in range(2, i + 1):
                if i % j == 0 and i != j:
                    break
                elif i % j == 0 and i == j:
                    counter += 1
            if counter == a:
                return i

print(timeit.timeit("prime_num(10)", number=100, globals=globals()))    # 0.0012069000000000003
print(timeit.timeit("prime_num(100)", number=100, globals=globals()))   # 0.138494
print(timeit.timeit("prime_num(1000)", number=100, globals=globals()))  # 25.7499497

cProfile.run('prime_num(10)')   # 1    0.000    0.000    0.000    0.000 task4_2.py:13(prime_num)
cProfile.run('prime_num(100)')  # 1    0.001    0.001    0.001    0.001 task4_2.py:13(prime_num)
cProfile.run('prime_num(1000)') # 1    0.252    0.252    0.252    0.252 task4_2.py:13(prime_num)


def sieve_eratos(num, n=1000):
    try:
        sieve = [item for item in range(n)]
        sieve[1] = 0

        for item in range(2, n):
            if sieve[item] != 0:
                k = item + item
                while k < n:
                    sieve[k] = 0
                    k += item

        res = [item for item in sieve if item != 0]
        result = res[num - 1]

        return result
    except IndexError:
        n += 1000
        return sieve_eratos(num, n)



print(timeit.timeit("sieve_eratos(10)", number=100, globals=globals()))   # 0.015297900000000197
print(timeit.timeit("sieve_eratos(100)", number=100, globals=globals()))  # 0.01573409999999953
print(timeit.timeit("sieve_eratos(1000)", number=100, globals=globals())) # 0.6129630999999982

cProfile.run('sieve_eratos(10)')      # 1    0.000    0.000    0.000    0.000 task4_2.py:35(sieve_func)
cProfile.run('sieve_eratos(100)')     # 1    0.000    0.000    0.000    0.000 task4_2.py:35(sieve_func)

cProfile.run('sieve_eratos(1000)')  # 8/1    0.005    0.001    0.006    0.006 task4_2.py:35(sieve_func)
                                    # 8      0.001    0.000    0.001    0.000 task4_2.py:37(<listcomp>)
                                    # 8      0.001    0.000    0.001    0.000 task4_2.py:47(<listcomp>)

# Функция с решетом Эратосфена эффективнее.