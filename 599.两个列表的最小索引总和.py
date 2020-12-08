#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        adict = {val: index for index, val in enumerate(list1)}
        alist = []
        min_index = float('inf')
        for index, val in enumerate(list2):
            if val in adict:
                s_index = index+adict[val]
                if s_index<min_index:
                    min_index = s_index
                    alist = [val]
                elif s_index == min_index:
                    alist.append(val)
        return alist

# @lc code=end

