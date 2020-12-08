#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List
from heapq import heapify, heappush
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i: i+k]) for i in range(len(nums)-k+1)]
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [max(nums[:k])]
        for i in range(1, len(nums)-k+1):
            if nums[i-1] == res[-1]:
                res.append(max(nums[i:i+k]))
            else:
                res.append(max(res[-1], nums[i+k-1]))
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        large_count = len(nums)+1-k
        larges = set(sorted(nums)[-large_count:])
        cur_larges = []
        for val in nums[:k]:
            if val in larges:
                cur_larges.append(val)
        res = [max(cur_larges)]
        for i in range(1, len(nums)-k+1):
            remove_num = nums[i-1]
            new_num = nums[i+k-1]
            if remove_num in larges:
                cur_larges.remove(remove_num)
            if new_num in larges:
                cur_larges.append(new_num)
            if remove_num == res[-1]:
                res.append(max(cur_larges))
            else:
                res.append(max(res[-1], new_num))
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        large_count = len(nums)+1-k
        larges = set(sorted(nums)[-large_count:])
        cur_larges = []
        for val in nums[:k]:
            if val in larges:
                cur_larges.append(val)
        res = [max(cur_larges)]
        for i in range(1, len(nums)-k+1):
            remove_num = nums[i-1]
            new_num = nums[i+k-1]
            if remove_num in larges:
                cur_larges.remove(remove_num)
            if new_num in larges:
                cur_larges.append(new_num)
            if remove_num == res[-1]:
                res.append(max(cur_larges))
            else:
                res.append(max(res[-1], new_num))
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        for index in range(k):
            while queue and nums[index] >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
        res = [nums[queue[0]]]
        for index in range(k, len(nums)):
            while queue and nums[index] >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
            if queue[0] < index-k+1:
                queue.popleft()
            res.append(nums[queue[0]])
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        res = []
        for index in range(len(nums)):
            while queue and nums[index] >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
            if index >=k-1:
                if queue[0] < index-k+1:
                    queue.popleft()
                res.append(nums[queue[0]])
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        res = []
        for index in range(len(nums)):
            while queue and nums[index] >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
            if queue[0] < index-k+1:
                queue.popleft()
            res.append(nums[queue[0]])
        return res[k-1:]

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = list()
        res = []
        for index in range(len(nums)):
            while queue and nums[index] >= nums[queue[-1]]:
                queue.pop()
            queue.append(index)
            if queue[0] < index-k+1:
                queue.pop(0)
            res.append(nums[queue[0]])
        return res[k-1:]
# @lc code=end

