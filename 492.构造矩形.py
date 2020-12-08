#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width =  2
        length = area
        while width**2 <= area:
            if not area % width:
                length = area // width
            width += 1
        return [length, area//length]
# @lc code=end

