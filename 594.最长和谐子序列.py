#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        res = 0
        length = len(nums)
        for i in range(length):
            is_flag = False
            count = 0
            for j in range(length):
                if nums[i] == nums[j]:
                    count += 1
                elif nums[j] + 1 == nums[i]:
                    count += 1
                    is_flag = True
            if is_flag:
                res = max(res, count)
        return res
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        res = 0
        for val in set(nums):
            if counter[val+1]:
                res = max(counter[val]+counter[val+1], res)
        return res
    def findLHS(self, nums: List[int]) -> int:
        from collections import defaultdict
        adict = defaultdict(int)
        res = 0
        for val in nums:
            adict[val] += 1
            if adict[val+1]:
                res = max(res, adict[val]+adict[val+1])
            if adict[val-1]:
                res = max(res, adict[val]+adict[val-1])
        return res



# @lc code=end

