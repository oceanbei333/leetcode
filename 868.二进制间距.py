#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        nums = bin(n)[2:]
        if nums.count("1") < 2:
            return 0
        pre = 0
        dis = 1
        for index in range(1, len(nums)):
            if nums[index] == '1':
                dis = max(dis, index-pre)
                pre = index
        return dis
# @lc code=end

