#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        cur_left = 100
        rows = 1
        for s in S:
            needs = widths[ ord(s)-ord('a') ]
            if needs > cur_left:
                rows += 1
                cur_left = 100 - needs
            else:
                cur_left -= needs
        return rows, 100-cur_left
        
# @lc code=end

