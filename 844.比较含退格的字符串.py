#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        alist = []
        for s in S:
            if s == "#":
                if alist:
                    alist.pop()
            else:
                alist.append(s)
        blist = []
        for s in T:
            if s == "#":
                if blist:
                    blist.pop()
            else:
                blist.append(s)
        return alist == blist
        
# @lc code=end

