#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = len(g)
        j = len(s)
        res = 0
        while i and j:
            if s[j-1] >=g[i-1]:
                res += 1
                j -= 1
            i -= 1
        return res


# @lc code=end

