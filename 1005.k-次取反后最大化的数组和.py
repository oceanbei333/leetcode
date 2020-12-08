#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
from heapq import heappush, heapreplace
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heap = []
        for val in A:
            heappush(heap, val)
        for _ in range(K):
            heapreplace(heap, -heap[0])
        return sum(heap)
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heap = []
        res = 0
        for val in A:
            heappush(heap, val)
            res += val
        for _ in range(K): 
            res -= 2*heap[0]  
            heapreplace(heap, -heap[0])
        return res
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heap = []
        for val in A:
            heappush(heap, val)
        for index in range(K):
            if heap[0]>=0:
                if (K-index)%2:
                    return sum(heap) - 2*heap[0]
                else:
                    return sum(heap)
            heapreplace(heap, -heap[0])
        return sum(heap)
# @lc code=end

