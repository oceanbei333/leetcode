#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        aset = {"a", "o", "i", "u", "e"}
        alist = [ index for index in range(len(s)) if s[index].lower() in aset ]
        c_list = list(s)
        for index in range(len(alist)//2):
            i = alist[index]
            j = alist[-index-1]
            c_list[i], c_list[j] = c_list[j], c_list[i]
        return ''.join(c_list)
            
        
# @lc code=end

