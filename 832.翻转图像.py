#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        l_r = len(A)
        l_c = len(A[0])
        for r in range(l_r):
            for c in range((l_c+1)//2):
                A[r][c], A[r][l_c-1-c] = A[r][l_c-1-c]^1, A[r][c]^1
        return A


        
# @lc code=end

