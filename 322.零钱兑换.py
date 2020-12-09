#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List, Union
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_set =  set(coins)
        paths = []
        @functools.lru_cache(None)
        def _coinChange(amount:int, steps:int):
            if not amount:
                paths.append(steps)
                return
            if amount < 0:
                return
            for val in coin_set:
                _coinChange(amount-val, steps+1)
        _coinChange(amount, 0)
        return min(paths) if paths else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        from collections import deque
        queue = deque([(amount, 0)])
        while queue:
            root, depth = queue.popleft()
            if not root:
                return depth
            for val in coins:
                new_root =  root-val
                if new_root >= 0:
                    queue.append((new_root, depth+1))
        return -1
    def coinChange(self, coins: List[int], amount: int) -> Union[float, int ]:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if coin <=i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[-1] > amount else dp[-1]
# @lc code=end

