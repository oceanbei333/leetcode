#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [s for s in S if s.isalpha()]
        return ''.join(letters.pop() if s.isalpha() else s for s in S)

    def reverseOnlyLetters(self, S: str) -> str:
        res = ''
        i = len(S) - 1
        for s in S:
            if s.isalpha():
                while not S[i].isalpha():
                    i -= 1
                res += S[i]
                i -= 1
            else:
                res += s
        return res

# @lc code=end
