#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        adict = {val: index+1 for index, val in enumerate(arr2)}
        return list(sorted(arr1, key=lambda x:  adict.get(x) or x+1+len(arr2)))
        
# @lc code=end

