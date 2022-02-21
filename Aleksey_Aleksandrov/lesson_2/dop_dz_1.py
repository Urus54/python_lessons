# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s)//2):
            s[idx], s[-idx-1] = s[-idx-1], s[idx]


# Accepted
# Runtime: 42 ms
# Your input
# ["h","e","l","l","o"]
# Output
# ["o","l","l","e","h"]
# Expected
# ["o","l","l","e","h"]