#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0 
        for  index in range(len(arr)):
            if arr[index]%2:
                count += 1
            else:
                count = 0
            if count >2:
                return True 
        return False


# @lc code=end

