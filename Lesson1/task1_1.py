""""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


https://drive.google.com/file/d/19bi9Sn0VrcRKKYe007c0B5dzVULLRIl4/view?usp=sharing
"""
abc = int(input('Введите трехзначное челое число: '))

a = abc % 10
b = abc % 100 // 10
c = abc // 100
summ = a + b + c
prod = a * b * c

print("Сумма цифр числа:", summ)
print("Произведение цифр числа:", prod)
