#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        length = len(mat)
        for i in range(length):
            total += mat[i][i]
            total += mat[i][length-i-1]
        if length%2:
            total -= mat[length//2][length//2]
        return total

    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        num  = mat[length//2][length//2] if length%2 else 0
        return sum(mat[i][length-i-1]+mat[i][i] for i in range(length)) - num




# @lc code=end

