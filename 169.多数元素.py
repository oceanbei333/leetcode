#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def _majorityElement(alist: List[int]) -> int:
            if len(alist) == 1:
                return alist[0]
            mid = len(alist) // 2
            m_left = _majorityElement(alist[:mid])
            m_right = _majorityElement(alist[mid:])
            if m_right == m_left:
                return m_left
            counter_left = len(
                [i for i in alist if i == m_left])
            counter_right = len(
                [i for i in alist if i == m_right])
            return m_left if counter_left > counter_right else m_right
        return _majorityElement(nums)

    def majorityElement(self, nums: List[int]) -> int:
        while True:
            candidate = random.choice(nums)
            if len([1 for val in nums if val == candidate]) > len(nums)//2:
                return candidate

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        count = 1
        for val in nums[1:]:
            if val == num:
                count += 1
            else:
                if not count:
                    num = val
                    count += 1
                else:
                    count -= 1
        return num

    def majorityElement(self, nums: List[int]) -> int:
        def _majorityElement(nums: List[int]):
            if len(nums) == 1:
                return nums[0]
            mid = len(nums)//2
            majority_left = _majorityElement(nums[:mid])
            majority_right = _majorityElement(nums[mid:])
            if majority_left == majority_right:
                return majority_left
            if nums.count(majority_left) > nums.count(majority_right):
                return majority_left
            else:
                return majority_right
        return _majorityElement(nums)


# @lc code=end
