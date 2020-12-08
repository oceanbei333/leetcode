#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        for index in range(1, len(nums)):
            nums[index] += nums[index-1]
        self.nums = nums


    @functools.lru_cache(None)
    def sumRange(self, i: int, j: int) -> int:
        if not i:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

