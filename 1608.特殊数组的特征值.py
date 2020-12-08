#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        for i in range(1, length+1):
            for  j in range(length):
                if nums[j] >= i:
                    if length-j ==i:
                        return i
                    else:
                        break
        return -1
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        adict = { nums[0]:1 }
        for index in range(1, len(nums)):
            if nums[index] in adict:
                adict[nums[ index ]] += 1
            else:
                adict[nums[ index ]] = adict[nums[ index-1 ]]
        bdict = {}
        for i in range(1, len(nums)+1):
            bdict[i]
        return -1

# @lc code=end

