#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] 二进制矩阵中的特殊位置
#

# @lc code=start
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sum_r = {r for r, row in enumerate(mat) if sum(row)==1}
        sum_c = set()
        for i in range(len(mat[0])):
            if sum(mat[j][i] for j in range(len(mat)) ) == 1:
                sum_c.add(i)
        return sum(mat[r][c]==1 for r in sum_r for c in sum_c)

    def numSpecial(self, mat: List[List[int]]) -> int:
        return sum(   
            mat[r][c]==sum(row)== sum(col)==1 
            for r, row in enumerate(mat) 
            for c, col in enumerate(zip(*mat)) 
        ) 



# @lc code=end

