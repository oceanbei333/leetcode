#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        intervals.append([float('inf'), float('inf')])
        res = []
        for i in range(len(intervals)-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                if intervals[i][1] > intervals[i+1][1]:
                    intervals[i+1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res


# @lc code=end
