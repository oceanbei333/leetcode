#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and not x%10):
            return False
        return str(x) == (str(x)[::-1])
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and not x%10):
            return False
        s = str(x)
        return all(s[index]==s[-index-1] for index in range(len(s)//2) )
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and not x%10):
            return False
        y = x
        z = 0
        while y:
            z = z*10+y%10
            y //= 10
        return x ==z

            
# @lc code=end

