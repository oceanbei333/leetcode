#
# @lc app=leetcode.cn id=1486 lang=python3
#
# [1486] 数组异或操作
#

# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = start
        for i in range(1, n):
            num ^= start + 2*i
        return num
    def xorOperation(self, n: int, start: int) -> int:
        return functools.reduce(lambda x,y: x^(start+2*y), (0, *range(n)))


# @lc code=end

