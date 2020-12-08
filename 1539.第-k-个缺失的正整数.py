#
# @lc app=leetcode.cn id=1539 lang=python3
#
# [1539] 第 k 个缺失的正整数
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for index in range(len(arr)):
            if arr[index] - index-1 >= k:
                return arr[index] -(arr[index]-index-k)
        return arr[-1] -(arr[-1]-len(arr)-k)
# @lc code=end

