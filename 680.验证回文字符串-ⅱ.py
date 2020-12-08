#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for index in range(len(s)):
            astr = s[:index]+s[index+1:]
            if astr == astr[::-1]:
                return True
        return False
        
    def validPalindrome(self, s: str) -> bool:
        def check(s:str) -> bool:
            low = 0
            high = len(s) -1
            while low < high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True
        low = 0
        high = len(s) -1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return check(s[low+1:high+1]) or check(s[low:high])
        return True
# @lc code=end

