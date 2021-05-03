""""
1. Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

"""

from collections import defaultdict

QUARTERS = 4
total_companies = int(input('Введите количество предприятий: '))
info = defaultdict(list)
average = 0

for i in range(total_companies):
    name = input('Введите название предприятия: ')
    for j in range(QUARTERS):
        info[name].append(int(input(f'Введите количество прибыли за {j + 1}-й квартал: ')))
    info[name] = sum(info[name])
    average += info[name]

average = average / total_companies

print('Средняя прибыль предприятий равна:', average)

for name in info:
    if info[name] > average:
        print('Предприятие с доходом выше среднего:', name)
    elif info[name] < average:
        print('Предприятие с доходом ниже среднего:', name)
