#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for index in range(1,n):
            if not str(index).count('0') and not str(n-index).count('0'):
                return index, n-index
        
# @lc code=end

