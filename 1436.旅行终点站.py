#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from graphlib import TopologicalSorter
        adict = {}
        for key, value in paths:
            adict[value] = {key}
        ts = TopologicalSorter(adict)
        return tuple(ts.static_order())[-1]
    def destCity(self, paths: List[List[str]]) -> str:
        srcs = set()
        dsts = set()
        for src, dst in paths:
            srcs.add(src)
            dsts.add(dst)
        return (dsts-srcs).pop()
# @lc code=end

