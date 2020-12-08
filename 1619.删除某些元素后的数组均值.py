#
# @lc app=leetcode.cn id=1619 lang=python3
#
# [1619] 删除某些元素后的数组均值
#

# @lc code=start
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        num = len(arr)//20
        return sum(arr[num: len(arr)-num])/(len(arr)-2*num)
# @lc code=end

