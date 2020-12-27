#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        target = len(nums)//3
        return [num for num, count in counter.items() if count > target]

    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, count1, count2 = None, None, 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            else:
                if not count1:
                    cand1 = num
                    count1 = 1
                elif not count2:
                    cand2 = num
                    count2 = 1
                else:
                    count1 -= 1
                    count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        res = []
        if count1 > len(nums)//3:
            res.append(cand1)
        if count2 > len(nums)//3:
            res.append(cand2)
        return res


# @lc code=end
