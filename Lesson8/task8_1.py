"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.

"""
import hashlib


def count_substr(my_string):
   for i in range(len(my_string)):
        for j in range(len(my_string), i, -1):
            hash_str = hashlib.sha1(my_string[i:j].encode('utf-8')).hexdigest()
            _sum.add(hash_str)
    return len(_sum) - 1


_sum = set()
my_string = input('Введите строку: ')
print(f'Количество подстрок в строке {my_string}: {count_substr(my_string)}')

"""
Спасибо за прекрасный курс, с такими хорошими преподавателями судьба сводит всего несколько раз в жизни,
надеюсь ещё встретиться с вами.

"""