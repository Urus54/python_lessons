# Учитывая целочисленный массив nums,
# переместите все 0 в его конец,
# сохраняя относительный порядок
# ненулевых элементов.

nums = [0,1,0,3,0,12]
n = len(nums)
j = 0
for i in range(n):
    nums[j] = nums[i]
    j += 1 if nums[i] else 0
nums[j:] = [0] * (n-j)

print(nums)