# Представлен список чисел.
# Необходимо вывести те его элементы, значения которых больше предыдущего.

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [val for idx, val in enumerate(src) if src[idx - 1] < src[idx] and idx > 0]

print(result)