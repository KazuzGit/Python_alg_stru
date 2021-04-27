""""
4. Определить, какое число в массиве встречается чаще всего.

"""

from random import randint

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

counts = dict()

for i in array:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print(counts)

max_item = 0
max_ = 0

for key, item in counts.items():
    if item > max_:
        max_item = key
        max_ = item

print(f'Чаще всего встречается число {max_item}')
