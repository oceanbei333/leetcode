#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)

        def _permuteUnique(used: list, unused: list):
            if not unused:
                res.append(used)
            for i in range(len(unused)):
                _permuteUnique(used+unused[i:i+1], unused[:i]+unused[i+1:])
        _permuteUnique([], nums)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def _permute(used: list):
            if len(used) == n:
                res.append(used)
                return
            for val in set(nums)-set(used):
                _permute(used+[val])
        _permute([])
        return res

    def permuteUnique(self, nums):
        def backtrack(index: int):
            if index == n:
                res.append(nums[:])
                return
            backtrack(index + 1)
            for i in range(0, index):
                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        n = len(nums)
        res = []
        backtrack(0)
        return res

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                # nums[:first] 已经使用的元素
                # nums[first:] 可以使用的元素
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack(0)
        return res



# @lc code=end
