# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел
# в интервале от 1 до 100:

percent = int(input("Введите число "))

for percent in range(101):
    if percent % 10 == 1 and percent % 100 !=11:
        print(percent,"процент")
    elif 1< percent % 10 < 5 and not 11 < percent % 100 <15:
        print(percent,"процента")
    else:
        print(percent,"процентов")
