#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name or not typed:
            return False
        if name[0] != typed[0] or name[-1]!=typed[-1]:
            return False
        i = j = 0
        while j < len(typed):
            if typed[j] == name[i]:
                j += 1
                if i < len(name)-1:
                    i+= 1
            else:
                if typed[j] == name[i-1]:
                    j+=1
                else:
                    return False
        return i == len(name)-1
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i =j = 0
        while j < len(typed):
            if i < len(name) and typed[j] == name[i]:
                i += 1
                j += 1
            elif i> 0 and typed[j] == name[i-1]:
                j += 1
            else:
                return False
        return i == len(name)


# @lc code=end

