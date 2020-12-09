#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        while not n % 2:
            n //= 2
        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        return not n & (n-1)

    def isPowerOfTwo(self, n: int) -> bool:
        if not n:
            return False
        while not n & 1:
            n >>= 1
        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        nums = bin(n)
        return nums[0] != '-' and nums.count('1') == 1
# @lc code=end
