#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 1
        for index in range(1,len(nums)):
            if nums[index] != nums[index-1]:
                nums[cur] = nums[index]
                cur += 1
        return cur
    def removeDuplicates(self, nums: List[int]) -> int:
        alist=sorted(set(nums))
        nums[:len(alist)] = alist
        return len(alist)

    def removeDuplicates(self, nums: List[int]) -> int:
        dup_count = 0
        for index in range(1, len(nums)):
            if nums[index] != nums[index-1]:
                nums[index-dup_count] = nums[index]
            else:
                dup_count += 1
        return len(nums) - dup_count


        

# @lc code=end
