#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def _combine(level:int, start:int, alist:list):
            if not level:
                res.append(alist)
                return
            for i in range(start, n+2-level):
                _combine(level-1, i+1,alist.copy() + [i])
        _combine(k,1, [])
        return res
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return list(combinations(range(1, n+1), k))
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = list(range(1,k+1)) +[n+1]
        j = 0
        while j<k:
            res.append(temp[:k])
            j = 0
            # 从后固定值，前面以等差数列的形式追赶
            while j<k and temp[j] +1 == temp[j+1]:
                temp[j] = j+1
                j+=1
            temp[j] += 1
        return res

# @lc code=end

