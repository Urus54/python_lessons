# Удалить дубликаты из отсортированного массива

array = [2, 2, 5, 5, 7, 7, 9, 9]
ind = 1
while ind < len(array):
    if array[ind] in array[ : ind]:
        array.pop(ind)
    else:
        ind += 1

print(array)
