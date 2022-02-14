# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

n = int(input("Введите трехзначное число: "))

sum = 0
mult = 1

while n > 0:
    digit = n % 10
    if digit != 0:
        sum += digit
        mult *= digit
    n = n // 10

print("Сумма:", sum)
print("Произведение:", mult)