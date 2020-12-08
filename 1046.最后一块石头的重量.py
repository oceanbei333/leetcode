#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
from typing import List
from heapq import heappush, heappop, heapreplace
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heappush(heap, -weight)
        for _ in range(len(stones)-1):
            heapreplace(heap, heappop(heap)- heappop(heap))
        return -heap[0]
        
    def lastStoneWeight(self, stones: List[int]) -> int:
        for _ in range(len(stones)-1):
            large = max(stones)
            stones.remove(large)
            small = max(stones)
            stones.remove(small)
            diff = large - small
            stones.append(diff)
        return stones[0]
    def lastStoneWeight(self, stones: List[int]) -> int:
        for _ in range(len(stones)-1):
            stones.sort()
            diff = stones.pop() - stones.pop()
            stones.append(diff)
        return stones[0]



# @lc code=end

