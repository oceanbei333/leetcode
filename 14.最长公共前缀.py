#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        length  = min(len(s) for s in strs )
        if not length:
            return ''
        for index in range(length):
            if not len({ s[index] for s in strs })==1:
                return ''.join(strs[0][:index])
        return ''.join(strs[0][:index+1])
            
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]
        for str_ in strs[1:]:
            if not result:
                return result
            for index, ( s1, s2 ) in enumerate(zip(result, str_)):
                print(index, s1, s2)
                if s1 !=s2:
                    result = result[:index]
            else:
                result = result[:min(len(result), index)]
        return result

# @lc code=end

