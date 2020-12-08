#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target_num = len(arr) // 4
        for num, count in collections.Counter(arr).items():
            if count > target_num:
                return num
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        span = n // 4 + 1
        for i in range(0, n, span):
            iter_l = bisect.bisect_left(arr, arr[i])
            iter_r = bisect.bisect_right(arr, arr[i])
            if iter_r - iter_l >= span:
                return arr[i]
        return -1

# @lc code=end

