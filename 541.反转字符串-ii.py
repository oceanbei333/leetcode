#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        alist = []
        while index < len(s):
            if not index:
                alist.extend(s[index+k-1::-1])
            else:
                alist.extend(s[index+k-1:index-1:-1])
            alist.extend(s[index+k: index+2*k])
            index += 2*k
        return ''.join(alist)
# @lc code=end

