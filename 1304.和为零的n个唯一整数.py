#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的N个唯一整数
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range(1, n//2+1):
            result.append(i)
            result.append(-i)
        if n%2:
            result.append(0)
        return result
    def sumZero(self, n: int) -> List[int]:
        result = list( range(n-1) )
        result.append(-(n-2)*(n-1)//2)
        return result



# @lc code=end

