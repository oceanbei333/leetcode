#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        length = len(stones)

        @functools.lru_cache(None)
        def dp(index: int, k: int):
            if index >= length-1:
                return True
            for i in range(index+1, length):
                diff = stones[i] - stones[index]
                if diff in {k-1, k, k+1}:
                    if dp(i, diff):
                        return True
                elif diff > k+1:
                    break
            return False
        return dp(0, 0)

    def canCross(self, stones: List[int]) -> bool:
        length = len(stones)
        from collections import deque
        queue = deque([(0, 0)])
        aset = {(0, 0)}
        while queue:
            index, k = queue.popleft()
            if index == length-1:
                return True
            for i in range(index+1, length):
                diff = stones[i] - stones[index]
                if diff in {k-1, k, k+1}:
                    if (i, diff) not in aset:
                        aset.add((i, diff))
                        queue.append((i, diff))
                elif diff > k+1:
                    break
        return False

    def canCross(self, stones: List[int]) -> bool:
        stones_set = set(stones)
        from collections import defaultdict
        dp = defaultdict(set)
        dp[0].add(0)
        for i in stones:
            k_set = dp[i]
            for k in k_set:
                for j in (k-1, k, k+1):
                    if j > 0 and (i+j) in stones_set:
                        dp[i+j].add(j)
        return bool(dp[stones[-1]])

    def canCross(self, stones: List[int]) -> bool:
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        for i in stones:
            for k in dp[i]:
                for j in (k-1, k, k+1):
                    if j > 0 and (i+j) in dp:
                        dp[i+j].add(j)
        return bool(dp[stones[-1]])
# @lc code=end
