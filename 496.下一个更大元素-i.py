#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        adict = dict()
        aset = set(nums1)
        for i in range(len(nums2)):
            if nums2[i] in aset:
                for j in range(i+1, len(nums2)):
                    if nums2[j] >nums2[i]:
                        adict[nums2[i]] = nums2[j]
                        break
        return [adict.get(val, -1) for val in nums1]
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        adict = dict()
        for val in nums2:
            while stack and val > stack[-1]:
                adict[stack.pop()] = val
            stack.append(val)
        return [adict.get(val, -1) for val in nums1]
        
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        adict = dict()
        for val in nums2[::-1]:
            while stack and  val < stack[-1]:
                stack.pop()
            if stack:
                adict[val] = stack[-1]
            stack.append(val)
        return [adict.get(val, -1) for val in nums1]



        
# @lc code=end

