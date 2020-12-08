#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        for index in range(x+1):
            if index **2 == x:
                return index
            elif index ** 2 >x:
                return index-1

    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = -1
        while low <= high:
            mid = (low+high)//2
            num = mid**2
            if num <= x:
                ans = mid
                low = mid+1
            else :
                high = mid-1
        return ans
        


# @lc code=end

