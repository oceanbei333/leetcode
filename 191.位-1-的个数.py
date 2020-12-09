#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= (n-1)
        return count

    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n //= 2
        return count

# @lc code=end
