# 231. Power of Two
# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0, n + 1):
            if self.power(2, i) == n:
                return True
            elif self.power(2, i) > n:
                return False

        return False

    def power(self, a, b):
        if b == 0:
            return 1

        if b == 1:
            return a

        if b % 2 == 0:
            return self.power(a * a, b // 2)
        else:
            return self.power(a * a, b // 2) * a

# Accepted
# Runtime: 54 ms

# Your input
# 1
# 16
# 3
# Output
# true
# true
# false

# Expected
# true
# true