#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min_val = float('inf')
        min_index = None
        n = len(nums)
        mins = list(range(n))
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_index = i
            else:
                mins[i] = min_index
        print(mins)

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        r, l = 0, n-1
        for i in range(n):
            for j in range(i+1, n):
                if r - l + 1 == n:
                    return n
                if nums[i] > nums[j]:
                    l = min(l, i)
                    r = max(r, j)
        return r - l+1 if r > l else 0

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        n = len(nums)
        l = 0
        r = n-1
        for i in range(n):
            l = i
            if nums[i] != sorted_nums[i]:
                break
        for j in range(n-1, -1, -1):
            r = j
            if nums[j] != sorted_nums[j]:
                break
        return r - l+1 if r > l else 0
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = [-1]
        n = len(nums)
        nums.append(float('-inf'))
        l = 0
        for i in range(n):
            if nums[i] >= nums[stack[-1]]:
                stack.append(i)
            else:
                while stack[-1] > nums[i]:
                    l = stack.pop()
        nums[-1] = float('inf')
        stack.append(n)
        for j in range(n-1, -1, -1):
            if nums[j] <= nums[stack[-1]]:
                stack.append(j)
            else:
                while stack[-1] < nums[j]:
                    r = stack.pop()
        

# @lc code=end
