# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()

        for num in nums:
            if num not in counter:
                counter.add(num)
            else:
                return True

        return False

# Accepted
# Runtime: 40 ms
# Your input
# [1,2,3,1]
# Output
# true
# Expected
# true