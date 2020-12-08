#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if len(s) == 1:
            return False
        if len(set(s)) == 1:
            return True
        nums = 3
        while nums <= length//2:
            if length % nums:
                nums += 2
                continue
            step = length//nums
            if all(s[index-step: index ]==s[index:index+step] for index in range(step, length, step)):
                return True
            nums+= 2
        return False
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for step in range(1, length//2+1):
            if not length%step:
                if all(s[index-step: index ]==s[index:index+step] for index in range(step, length, step)):
                    return True
        return False
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for step in range(1, length//2+1):
            if not length%step:
                if all(s[index]==s[index+step] for index in range(length-step)):
                    return True
        return False
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s+s).find(s, 1) != len(s)



        


        
# @lc code=end

