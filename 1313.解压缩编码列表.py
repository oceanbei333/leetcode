#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(0, len(nums), 2):
            result.extend([nums[index+1]]*nums[index])
        return result
# @lc code=end

