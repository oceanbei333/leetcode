#
# @lc app=leetcode.cn id=1309 lang=python3
#
# [1309] 解码字母到整数映射
#

# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        adict = {}
        for index in range(1, 10):
            adict[str(index)] = chr(ord('a')+index-1)
        for index in range(10,27):
            adict[f"{index}#"] = chr(ord('j')+index-10)
        res = ''
        index = len(s) -1
        while index >= 0:
            if s[index] == '#':
                res = adict[s[index-2: index+1]] + res
                index -= 3
            else:
                res = adict[s[ index ]] + res
                index -= 1
        return res

# @lc code=end

