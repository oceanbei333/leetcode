#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
from typing import List


class Solution:
    @functools.lru_cache(1)
    def get_nums(self, n: int) -> List[int]:
        return [i**2 for i in range(int(n**0.5), 0, -1)]

    @functools.lru_cache(None)
    def numSquares(self, n: int) -> int:
        if not n:
            return 0
        if n < 0:
            return n
        nums = self.get_nums(n)
        return min(self.numSquares(n-num)+1 for num in nums)

    def numSquares(self, n: int) -> int:
        queue = [(n, 0)]
        nums = self.get_nums(n)
        while queue:
            new_queue = []
            for n, depth in queue:
                for num in nums:
                    if not n - num:
                        return depth+1
                    if n - num > 0:
                        new_queue.append((n-num, depth+1))
            queue = new_queue

    def numSquares(self, n: int) -> int:
        from collections import deque
        queue = deque([(n, 0)])
        nums = self.get_nums(n)
        while queue:
            n, depth = queue.popleft()
            for num in nums:
                if not n - num:
                    return depth + 1
                if n - num > 0:
                    queue.append((n-num, depth+1))

    def numSquares(self, n: int) -> int:
        nums = self.get_nums(n)
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            for num in nums:
                if i == num:
                    dp[i] = 1
                elif num < i and dp[i-num]:
                    if dp[i]:
                        dp[i] = min(dp[i-num]+1, dp[i])
                    else:
                        dp[i] = dp[i-num] + 1
        return dp[-1]

    def numSquares(self, n: int) -> int:
        nums = self.get_nums(n)
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for num in nums:
                if num <= i:
                    dp[i] = min(dp[i-num]+1, dp[i])
        return dp[-1]

    def numSquares(self, n: int) -> int:
        nums = self.get_nums(n)
        def is_divided_by(n:int, count:int):
            if count == 1:
                return n in nums
            for num in nums:
                if is_divided_by(n-num, count-1):
                    return True
            return False
        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count


# @lc code=end
