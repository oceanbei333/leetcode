#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k


    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.nums = nums
        self.k = k


    def add(self, val: int) -> int:
        from bisect import insort
        insort(self.nums, val)
        return self.nums[-self.k]
from heapq import heappush, heappushpop
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        nums.sort()
        for val in nums[-k:]:
            heappush(self.heap, val)
        


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heappushpop(self.heap, val)
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

