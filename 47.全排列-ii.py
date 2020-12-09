#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        def _permuteUnique(first:int):
            if first ==n:
                res.add(tuple(nums[:]))
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                _permuteUnique(first+1)
                nums[i], nums[first] = nums[first], nums[i]
        _permuteUnique(0)
        return list(map(list, res))
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        def _permuteUnique(used:list, unused:list):
            if not unused:
                res.add(tuple(used))
            for i in range(len(unused)):
                _permuteUnique(used+unused[i:i+1], unused[:i]+unused[i+1:])
        _permuteUnique([], nums)
        return list(map(list, res))
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        def _permuteUnique(used:list, unused:list):
            if not unused:
                res.append(used)
            aset = set()
            for i in range(len(unused)):
                if unused[i] in aset:
                    continue
                else:
                    aset.add(unused[i])
                _permuteUnique(used+unused[i:i+1], unused[:i]+unused[i+1:])
        _permuteUnique([], nums)
        return res
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        def _permuteUnique(first:int):
            if first ==n:
                res.append(nums[:])
            aset = set()
            for i in range(first, n):
                if nums[i] not in aset:
                    aset.add(nums[i])
                    nums[first], nums[i] = nums[i], nums[first]
                    _permuteUnique(first+1)
                    nums[i], nums[first] = nums[first], nums[i]
        _permuteUnique(0)
        return res

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(current_len = 0):
            if current_len == n:  
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(0, current_len):
                if nums[i] == nums[current_len]:
                    return
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]
        nums.sort()
        n = len(nums)
        res = []
        backtrack()
        return res

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        def _permuteUnique(used:list, unused:list):
            if not unused:
                res.append(used)
            for val in set(unused):
                b_unused = unused.copy()
                b_unused.remove(val)
                _permuteUnique(used+[val], b_unused)
        _permuteUnique([], nums)
        return res


# @lc code=end

