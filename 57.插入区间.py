#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
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
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        flag = False
        res = []
        for l ,r in intervals:
            if l > right:
                if not flag:
                    res.append([left, right])
                    flag = True
                res.append([l, r])
            elif r < left:
                res.append([l, r])
            else:
                left = min(l, left)
                right = max(r, right)
        if not flag:
            res.append([left, right])
        return res


# @lc code=end
