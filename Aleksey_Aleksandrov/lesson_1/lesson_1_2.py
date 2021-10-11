# Создать список, состоящий из кубов нечётных чисел от 1 до 1000
# (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму,
# так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

cubes_list = []
cubes_list_add = []
sum_1 = 0

for i in range(1,1000,2):
    cubes_list.append(i**3)

for ind, val in enumerate(cubes_list):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7==0:
        sum_1 += cubes_list[ind]

print(sum_1)

for m in cubes_list:
    cubes_list_add.append(m + 17)

sum_2 = 0

for ind, val in enumerate(cubes_list_add):
    sum_digits = 0
    while val > 0:
        sum_digits += val % 10
        val //= 10
    if sum_digits % 7 == 0:
        sum_2 += cubes_list_add[ind]

print(sum_2)

# конторольные суммы
# 17485588610
# 15392909930