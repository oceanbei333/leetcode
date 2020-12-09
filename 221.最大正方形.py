#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
import functools
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        length = min(m, n)
        for l in range(length, 0, -1):
            for x in range(0, n-l+1):
                for y in range(0, m-l+1):
                    if all(val != '0' for row in matrix[x:x+l] for val in row[y:y+l]):
                        return l*l
        return 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        result = []

        @functools.lru_cache(None)
        def dp(x: int, y: int):
            if x < 0 or y < 0:
                return 0
            dp(x-1, y)
            dp(x, y-1)
            if matrix[x][y] == '1':
                l = 1
                if x and y:
                    small_l = dp(x-1, y-1)
                    if small_l:
                        for i in range(1, small_l+1):
                            if matrix[x][y-i] == '1' and matrix[x-i][y] == '1':
                                l += 1
                            else:
                                break
                result.append(l)
                return l
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp(n-1, m-1)
        return max(result)**2 if result else 0

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        for x in range(n):
            for y in range(m):
                matrix[x][y] = int(matrix[x][y])
        for x in range(1, n):
            for y in range(1, m):
                left_up = matrix[x-1][y-1]
                if matrix[x][y] and left_up:
                    for i in range(1, left_up+1):
                        if matrix[x][y-i] and matrix[x-i][y]:
                            matrix[x][y] += 1
                        else:
                            break
        l = max(max(row) for row in matrix)
        return l**2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[int(matrix[x][y]) for y in range(m)]for x in range(n)]
        for x in range(1, n):
            for y in range(1, m):
                left_up = dp[x-1][y-1]
                if dp[x][y] and left_up:
                    for i in range(1, left_up+1):
                        if dp[x][y-i] and dp[x-i][y]:
                            dp[x][y] += 1
                        else:
                            break
        l = max(max(row) for row in dp)
        return l**2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        @functools.lru_cache(None)
        def dp(x: int, y: int) -> int:
            if not x or not y:
                return int(matrix[x][y])
            if matrix[x][y] == '0':
                return 0
            return min(dp(x-1, y), dp(x, y-1), dp(x-1, y-1)) + 1
        l = 0
        for x in range(n):
            for y in range(m):
                l = max(l, dp(x, y))
        return l**2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        for x in range(n):
            for y in range(m):
                if matrix[x][y] == '1':
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])+1
        return max(max(row) for row in dp)**2
# @lc code=end
