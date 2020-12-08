#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    adict = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        alist = list()
        for c in s:
            if c in {'{', '[', '('}:
                alist.append(c)
            else:
                if not alist or alist.pop()!= self.adict[c]:
                    return False
        return not alist
    def isValid(self, s: str) -> bool:
        while '[]' in s or '{}' in s or '()' in s:
            s = s.replace('[]', '').replace('{}', '').replace('()', '')
        return not s
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        adict = {"(": ")", "[": "]", "{": "}"}
        for c in s:
            if c in adict:
                stack.append(c)
            else:
                if not stack or c != adict[stack.pop()]:
                    return False
        return not stack

# @lc code=end

