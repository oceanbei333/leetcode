#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        aset = set()
        def _subsets(nums:List[int]):
            aset.add(tuple(nums))
            for i in range(len(nums)):
                _subsets(nums[0:i]+nums[i+1:])
        _subsets(nums)
        return list(map(list, aset))
    def subsets(self, nums: List[int]) -> List[List[int]]:
        aset = set()
        def _subsets(level:int, alist:List[int], unused:List[int]):
            if not level:
                aset.add(tuple(sorted(alist)))
                return
            for i in range(len(unused)):
                _subsets(level-1, alist+unused[i:i+1], unused[:i]+unused[i+1:])
            _subsets(level-1, alist, unused)
        _subsets(len(nums), [], nums)
        return list(map(list, aset))
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _subsets(index:int, alist:List[int]):
            if index == len(nums):
                res.append(alist[:])
                return
            _subsets(index+1, alist)
            alist.append(nums[index])
            _subsets(index+1, alist)
            alist.pop()
        _subsets(0, [])
        return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _subsets(index:int, alist:List[int]):
            if index == len(nums):
                res.append(alist)
                return
            _subsets(index+1, alist.copy())
            alist.append(nums[index])
            _subsets(index+1, alist.copy())
        _subsets(0, [])
        return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _subsets(index:int, alist:List[int]):
            if index == len(nums):
                res.append(alist)
                return
            _subsets(index+1, alist)
            _subsets(index+1, alist+nums[index:index+1])
        _subsets(0, [])
        return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _subsets(level:int, alist:List[int]):
            if not level:
                res.append(alist)
                return
            _subsets(level-1, alist)
            _subsets(level-1, alist+nums[level-1:level])
        _subsets(len(nums), [])
        return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _subsets(level:int, alist:List[int]):
            if not level:
                res.append(alist[:])
                return
            _subsets(level-1, alist)
            alist.append(nums[level-1])
            _subsets(level-1, alist)
            alist.pop()
        _subsets(len(nums), [])
        return res

        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res.extend([ sub+[num] for sub in res])
        return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [ sub+[num] for sub in res]
        return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _subsets(index:int, alist:List[int]):
            res.append(alist)
            for i in range(index, len(nums)):
                _subsets(index+1, alist+nums[index:index+1])
        _subsets(0, [])
        return res



# @lc code=end

