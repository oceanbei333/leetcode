#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        left, count = 0, 1
        for index in range(1, len(S)):
            if S[index] == '(':
                count += 1
            else:
                count -= 1
            if not count:
                res.append(( left, index ))
                left = index+1
        return ''.join(S[left+1:right] for left, right in res)
        
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        count = 0
        for s in S:
            if s == '(' and count:
                res += s
            elif s == ')' and count >1:
                res += s
            count += 1 if s == '(' else -1
        return res
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for s in S:
            if s == '(':
                if stack:
                    res += s
                stack.append(s)
            else:
                stack.pop()
                if stack:
                    res += s
        return res
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for s in S:
            if s == '(':
                if stack:
                    res += s
                stack.append(1)
            else:
                stack.pop()
                if stack:
                    res += s
        return res
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = []
        for s in S:
            if s == '(':
                if stack:
                    res.append(s)
                stack.append(1)
            else:
                stack.pop()
                if stack:
                    res.append(s)
        return ''.join(res)
# @lc code=end

