#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#

# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return all(n1 ==n2 for n1, n2 in zip(target, arr))
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted((target)) == sorted(arr)
# @lc code=end

