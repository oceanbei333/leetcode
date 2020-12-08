#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = ['qwertyuiopQWERTYUIOP','ASDFGHJKLasdfghjkl','ZXCVBNMzxcvbnm']
        res = []
        for each in words:
            x,y,z = 0,0,0
            for j in each:
                if j in a[0]:
                    x += 1
                elif j in a[1]:
                    y += 1
                else:
                    z += 1
            if len(each)==x or len(each)==y or len(each)==z:
                res.append(each)
        return res

        
# @lc code=end

