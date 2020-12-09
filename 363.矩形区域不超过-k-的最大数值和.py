#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        res = float('-inf')
        for x in range(n):
            for y in range(m):
                dp[x][y] = dp[x-1][y] + dp[x][y-1] - \
                    dp[x-1][y-1] + matrix[x][y]
        for x1 in range(n):
            for y1 in range(m):
                for x2 in range(x1, n):
                    for y2 in range(y1, m):
                        area = dp[x2][y2] - dp[x2][y1-1] - \
                            dp[x1-1][y2] + dp[x1-1][y1-1]
                        if area <= k:
                            res = max(res, area)
        return res

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        print(row, col)
        res = float('-inf')
        for left in range(col):
            sum_ = [0]*(row+1)
            for right in range(left, col):
                for j in range(row):
                    sum_[j+1] += matrix[j][right]
                array = sum_.copy()
                for i in range(row):
                    array[i+1] += array[i]
                for i in range(row):
                    for j in range(i+1, row+1):
                        val = array[j]-array[i]
                        if val <= k:
                            res = max(res, val)
        return res
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float('-inf')
        for left in range(col):
            sum_ = [0]*row
            for right in range(left, col):
                for j in range(row):
                    sum_[j] += matrix[j][right]
                arr = [0]
                cur = 0
                for tmp in sum_:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)

        return res


# @lc code=end
