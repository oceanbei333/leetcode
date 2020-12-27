#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def dp(i: int, j: int) -> int:
            if not i*j:
                return i+j
            if word1[i-1] == word2[j-1]:
                return dp(i-1, j-1)
            return min(dp(i-1, j-1), dp(i, j-1), dp(i-1, j))+1
        return dp(len(word1), len(word2))

    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0]*(l2+1) for _ in range(l1+1)]
        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    continue
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        dp = list(range(len(word2)+1))
        for i in range(1, len(word1)+1):
            pre, dp[0] = dp[0], i
            for j in range(1, len(word2)+1):
                cur = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j-1], pre) + 1
                pre = cur
        return dp[-1]

    def minDistance(self, word1: str, word2: str) -> int:
        queue, depth, visit = {(word1, word2)}, 0, set()
        while queue:
            visit |= queue
            new_queue = set()
            for w1, w2 in queue:
                if w1 == w2:
                    return depth
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                new_queue |= {(w1[1:], w2[1:]), (w1, w2[1:]),
                              (w1[1:], w2)}-visit
            queue = new_queue
            depth += 1
        return depth

# @lc code=end
