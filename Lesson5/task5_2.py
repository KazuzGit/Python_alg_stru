""""
2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""

from collections import deque

NUMBER_SYST = 16

def hex_sum(num_1, num_2):
    sum_ = deque()
    to_other = 0
    if len(num_1) >= len(num_2):
        num_1, num_2 = deque(num_1), deque(num_2)
    else:
        num_2, num_1 = deque(num_1), deque(num_2)

    while num_1:
        if num_2:
            remains = table[num_1.pop()] + table[num_2.pop()] + to_other
        else:
            remains = table[num_1.pop()] + to_other
        to_other = 0
        if remains >= NUMBER_SYST:
            sum_.appendleft(table[remains - NUMBER_SYST])
            to_other = 1
        else:
            sum_.appendleft(table[remains])
    if to_other:
        sum_.appendleft('1')
    return sum_

def hex_product(num_1, num_2):
    sum_ = deque()
    if len(num_1) >= len(num_2):
        num_1, num_2 = deque(num_1), list(num_2)
    else:
        num_2, num_1 = list(num_1), deque(num_2)

    num_1_copy = num_1.copy()
    num_1_copy.reverse()
    temp = deque([deque() for _ in range(len(num_2))])
    for i in range(len(num_2)):
        digit = table[num_2.pop()]
        for j in range(len(num_1)):
            temp[i].appendleft(digit * table[num_1_copy[j]])
        for _ in range(i):
            temp[i].append(0)
    to_other = 0
    for _ in range(len(temp[-1])):
        remains = to_other
        for i in range(len(temp)):
            if temp[i]:
                remains += temp[i].pop()
        if remains >= NUMBER_SYST:
            sum_.appendleft(table[remains % NUMBER_SYST])
            to_other = remains // NUMBER_SYST
        else:
            sum_.appendleft(table[remains])
    if to_other:
        sum_.appendleft(table[to_other])
    return sum_

signs = '0123456789ABCDEF'
table = {}

for i in range(len(signs)):
    table[signs[i]] = i
for i in range(len(signs)):
    table[i] = signs[i]

num_1 = input('Введите 1-е шестнадцатиричное число: ').upper()
num_2 = input('Введите 2-е шестнадцатиричное число: ').upper()

print(f'Сумма чисел = {list(hex_sum(num_1, num_2))}')
print(f'Произвдение чисел = {list(hex_product(num_1, num_2))}')
