# В массиве случайных целых чисел поменять
# местами минимальный и максимальный элементы.

from random import random

n = 15
arr = [0] * n
for i in range(n):
    arr[i] = int(random() * 100)
    print(arr[i], end=" ")
print()

mn = 0
mx = 0
for i in range(n):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print("arr[%d]=%d arr[%d]=%d" % (mn + 1, arr[mn], mx + 1, arr[mx]))
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b

for i in range(15):
    print(arr[i], end=" ")
print()