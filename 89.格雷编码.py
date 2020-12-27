#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        codes = self.grayCode(n - 1)
        num = 1 << (n - 1)
        return codes + [num + x for x in codes[::-1]]
# @lc code=end
