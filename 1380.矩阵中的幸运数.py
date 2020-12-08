#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        rMin, cMax = [float('inf')]*r, [float('-inf')]*c
        for i in range(r):
            for j in range(c):
                rMin[i] = min(rMin[i], matrix[i][j])
                cMax[j] = max(cMax[j], matrix[i][j])
        r_set = set( rMin )
        return [val for val in cMax if val in r_set]

# @lc code=end
