#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        aset = set(J)
        return sum(s in aset for s in S)
        
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter
        c = Counter(S)
        return sum(c[s] for s in J)
# @lc code=end

