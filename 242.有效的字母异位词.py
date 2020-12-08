#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)
    
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram(self, s: str, t: str) -> bool:
        nums = [0]*26
        for c in s:
            nums[ord(c)-ord('a')] +=1
        for c in t:
            nums[ord(c)-ord('a')] -=1
        return all(not num for num in nums)


# @lc code=end

