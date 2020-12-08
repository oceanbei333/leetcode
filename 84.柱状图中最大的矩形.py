#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start

from typing import List, Optional, Union

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if not length:
            return 0
        res = 0
        for i in range(length):
            for j in range(i+1, length):
                res = max(res, min(heights[i:j+1])*(j-i+1))
        return max(res, *heights)
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if not length:
            return 0
        res = 0
        for i in range(length):
            left=right=i
            while left>=0 and heights[left] >= heights[i]:
                left -=1
            while right<length and heights[right] >= heights[i]:
                right +=1
            res = max(res, heights[i]*(right-left-1))
        return res
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        alist = list()
        stack = list()
        for i in range(length):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            alist.append(stack[-1] if stack else -1)
            stack.append(i)
        stack.clear()
        for i in range(length-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right = stack[-1] if stack else length
            alist[i] = (right-alist[i]-1)*heights[i]
            stack.append(i)
        return max(alist) if alist else 0

    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = [-1]
        res = 0
        for i in range(length+1):
            while stack[-1] != -1 and (i == length or heights[stack[-1]] > heights[i]):
                # h = stack.pop(), right = i, left = stack[-1]
                res = max(res, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return res
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = [0]*length
        right = [length]*length
        stack = []
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        return max(heights[i]*(right[i]-left[i]-1) for i in range(length)) if length else 0 
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = list()
        res = 0
        for i in range(length):
            while stack and heights[stack[-1]] > heights[i]:
                # h = stack.pop(), right = i, left = stack[-1]
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                right = i
                res = max(res,h*(right-left-1) )
            stack.append(i)
        while stack:
            # h = stack.pop(), right = i, left = stack[-1]
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            right = length
            res = max(res,h*(right-left-1) )
        return res
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights = [0] + heights + [0]
        res = 0
        for i in range(1, len(heights)):
            while  heights[stack[-1]] > heights[i]:
                # h = stack.pop(), right = i, left = stack[-1]
                res = max(res, heights[stack.pop()]*(i-stack[-1]-1))
            stack.append(i)
        return res
# @lc code=end

