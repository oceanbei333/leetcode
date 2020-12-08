#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 方阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(sorted( range(len(mat)), key= lambda index: sum(mat[index])))[:k]
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        alist = [ sum(nums) for nums in mat ]
        result = list(range(len(mat)))
        result.sort(key=lambda index: alist[index])
        return result[:k]


# @lc code=end

