""""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
   Например, если введено число 3486, то надо вывести число 6843.

"""
numb = int(input('Введите натуральное число: '))

rez_numb = 0

while (numb > 0):
    rez_numb = rez_numb * 10 + numb % 10
    numb //= 10

print(f"Обратное по порядку цифр число равно: {rez_numb}")
