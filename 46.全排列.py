#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _permute(level:int, alist:list):
            if not level:
                res.append(alist)
                return
            for val in set(nums)-set(alist):
                _permute(level-1, alist+[val])
        _permute(len(nums), [])
        return res
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _permute(level:int, alist:list, blist:list):
            if not level:
                res.append(alist)
                return
            for i in range(len(blist)):
                if not i:
                    clist = blist[i+1:]
                elif i == len(blist) -1:
                    clist = blist[:i]
                else:
                    clist = blist[:i] + blist[i+1:]
                _permute(level-1, alist+blist[i:i+1], clist)
        _permute(len(nums), [], nums)
        return res
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def _permute(level:int, alist:list, blist:list):
            if not level:
                res.append(alist)
                return
            for i in range(len(blist)):
                _permute(level-1, alist+blist[i:i+1], blist[:i] + blist[i+1:])
        _permute(len(nums), [], nums)
        return res
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(current_len:int ):
            if current_len == n:  
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(0, current_len):
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]
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
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = len(nums)
        def _permuteUnique(used:list, unused:list):
            if not unused:
                res.append(used)
            for i in range(len(unused)):
                _permuteUnique(used+unused[i:i+1], unused[:i]+unused[i+1:])
        _permuteUnique([], nums)
        return res


# @lc code=end

