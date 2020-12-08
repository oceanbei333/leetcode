#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        low = 0
        high = len(S)-1
        a_str = ''
        b_str = ''
        while low < high:
            if S[low].isalpha() and S[high].isalpha():
                a_str += S[high]
                b_str = S[low] + b_str
                low += 1
                high -= 1
            elif S[low].isalpha():
                b_str = S[high] + b_str
                high -= 1
            elif S[high].isalpha():
                a_str += S[low]
                low += 1
            else:
                a_str += S[low]
                b_str = S[high] + b_str
                low += 1
                high -= 1
        if low == high:
            a_str += S[low]

        return a_str +  b_str
    def reverseOnlyLetters(self, S: str) -> str:
        low = 0
        high = len(S)-1
        a_str = ''
        b_str = ''
        while low < high:
            if S[low].isalpha() and S[high].isalpha():
                a_str += S[high]
                b_str = S[low] + b_str
                low += 1
                high -= 1
            else:
                if not S[low].isalpha():
                    a_str += S[low]
                    low+=1
                if not S[high].isalpha():
                    b_str = S[high] + b_str
                    high-=1
        if low == high:
            a_str += S[low]
        return a_str +  b_str
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [s for s in S if s.isalpha()]
        res = []
        for s in S:
            if s.isalpha():
                res.append(letters.pop())
            else:
                res.append(s)
        return ''.join(res)
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [s for s in S if s.isalpha()]
        res = ''
        for s in S:
            res += letters.pop() if s.isalpha() else s
        return res
    def reverseOnlyLetters(self, S: str) -> str:
        res = ''
        i = len(S) -1
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

