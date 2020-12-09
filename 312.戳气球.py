#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# @lc code=start
from typing import List, Tuple


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dp(nums: List[int]) -> int:
            length = len(nums)
            if length == 1:
                return 0
            return max(dp(nums[:i]+nums[i+1:]) + nums[i-1]*nums[i]*nums[i+1] for i in range(length-1))
        return dp(nums+[1])

    def maxCoins(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(s: str) -> int:
            nums = s.split('-')
            length = len(nums)
            if length == 1:
                return 0
            res = max(dp('-'.join(nums[:i]+nums[i+1:])) + int(nums[i-1])
                      * int(nums[i])*int(nums[i+1]) for i in range(length-1))
            return res
        return dp('-'.join(map(str, nums+[1])))

    def maxCoins(self, nums: List[int]) -> int:
        @functools.lru_cache(None)
        def dp(nums: Tuple[int]) -> int:
            length = len(nums)
            if length == 1:
                return 0
            res = max(dp(tuple(nums[:i]+nums[i+1:]))+nums[i-1]
                      * nums[i]*nums[i+1] for i in range(length-1))
            return res
        return dp(tuple(nums+[1]))

    def maxCoins(self, nums: List[int]) -> int:

        # 构造树
        head = pre = [1, None]
        for num in nums:
            cur = [num, None]
            pre[1] = cur
            pre = cur

        def dp(head):
            # no node
            if not head[1]:
                return 0
            # only one node
            if not head[1][1]:
                return head[1][0]
            pre = head
            cur = head[1]
            res = 0
            while cur:
                _next = cur[1]
                # 删除当前节点
                pre[1] = _next

                # 处理最后一个节点
                next_val = _next[0] if _next else 1
                res = max(res, dp(head) + pre[0]*cur[0]*next_val)
                # 恢复当前节点
                pre[1] = cur
                pre, cur = cur, _next
            return res
        return dp(head)

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)

        @functools.lru_cache(None)
        def dp(left: int, right: int)->int:
            if right - left <= 1:
                return 0
            res = 0
            for i in range(left+1, right):
                res = max(res, dp(left, i)+dp(i, right) +
                          nums[left]*nums[i]*nums[right])
            return res
        return dp(-1, n)

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for length in range(1, n+1):
            for l in range(-1, n-length):
                r = l+length+1
                for i in range(l+1, r):
                    cand = dp[l][i]+dp[i][r]+nums[l]*nums[i]*nums[r]
                    dp[l][r] = max(dp[l][r], cand)
        return dp[-1][n]

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, -2, -1):
            for r in range(l + 2, n +1 ):
                for i in range(l + 1, r):
                    cand = dp[l][i]+dp[i][r]+nums[l]*nums[i]*nums[r]
                    dp[l][r] = max(dp[l][r], cand)
        return dp[-1][n]


# @lc code=end
