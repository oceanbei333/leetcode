#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        adict = defaultdict(int)
        for cpdomain in cpdomains:
            counts, domain = cpdomain.split(" ")
            cdomains = domain.split('.')
            for index in range(len(cdomains)):
                adict['.'.join(cdomains[index:])] += int(counts)
        return [ f"{value} {key}" for key, value in adict.items()]
# @lc code=end

