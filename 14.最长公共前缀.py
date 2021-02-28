#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        length = min(len(s) for s in strs)
        for index in range(length):
            if len({s[index] for s in strs}) != 1:
                return strs[0][:index]
        return strs[0][:length]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        result = strs[0]
        for str_ in strs[1:]:
            if not result:
                return result
            for index, (s1, s2) in enumerate(zip(result, str_)):
                if s1 != s2:
                    result = result[:index]
                    break
            else:
                if len(result) > len(str_):
                    result = str_
        return result

    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(start: int, end: int) -> str:
            if start > end:
                return ''
            if start == end:
                return strs[start]
            mid = (start+end) >> 1
            lcp_l, lcp_r = lcp(start, mid), lcp(mid+1, end)
            for i, (c1, c2) in enumerate(zip(lcp_l, lcp_r)):
                if c1 != c2:
                    return lcp_l[:i]
            return lcp_l if len(lcp_l) < len(lcp_r) else lcp_r

        return lcp(0, len(strs)-1)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        low = 0
        high = min(len(str_) for str_ in strs)
        while low < high:
            mid = (high+low+1) >> 1
            if len({str_[:mid] for str_ in strs}) == 1:
                low = mid
            else:
                high = mid - 1
        return strs[0][:low]


# @lc code=end
