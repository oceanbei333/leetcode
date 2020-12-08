#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        adict = dict()
        aset = set()
        worlds = s.split(" ")
        if len(worlds) != len(pattern):
            return False
        for c, word in zip(pattern, worlds):
            if c not in adict:
                if word in aset:
                    return False
                adict[c] = word
                aset.add(word)
            else:
                if adict[c] != word:
                    return False
        return True
# @lc code=end

