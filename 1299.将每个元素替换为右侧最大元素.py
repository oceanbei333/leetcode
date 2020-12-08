#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = arr[-1]
        arr[-1] = -1
        for index in range(1, len(arr)):
            val = arr[-index-1]
            arr[-index-1] = max_num
            max_num = max(val, max_num)
        return arr

        
# @lc code=end

