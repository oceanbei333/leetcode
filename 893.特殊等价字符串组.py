#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(word:str)->tuple:
            res = [0]*52
            for index, s in enumerate(word):
                res[ord(s)-ord('a')+26*(index%2)] += 1
            return tuple(res)
        return len({ count(word) for word in A })
# @lc code=end

