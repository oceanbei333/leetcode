#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        cur_max = 0
        for val in nums:
            if val:
                cur_max += 1
            else:
                max_num = max(cur_max, max_num)
                cur_max = 0
        return max(max_num, cur_max)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str, nums)).split('0')))
# @lc code=end
