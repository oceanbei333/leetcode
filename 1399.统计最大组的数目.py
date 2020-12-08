#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        adict = collections.defaultdict(int)
        for i in range(1, n+1):
            adict[sum(map(int, str(i)))] += 1
        max_n = max(adict.values())
        return sum(max_n ==s for s in adict.values())

# @lc code=end

