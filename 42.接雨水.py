#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
from _typeshed import StrPath


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        stack = []
        left = [0]*length
        right = [0]*length
        for i in range(length):
            while stack and height[stack[-1]] < height[i]:
                stack.pop()
            stack.append(i)
            left[i] = stack[0]
        stack.clear()
        for i in range(length-1, -1, -1):
            while stack and height[stack[-1]] < height[i]:
                stack.pop()
            stack.append(i)
            right[i] = stack[0]
        res = 0
        for i in range(length):
            res += min(height[left[i]], height[right[i]])-height[i]
        return res
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            left = max(height[:i+1])
            right = max(height[i:])
            area = min(left, right)-height[i]
            res += area
        return res
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        length = len(height)
        left = [height[0]]
        for i in range(1,length):
            left.append(height[i] if left[-1] < height[i] else left[-1])
        right = [height[-1]]
        for i in range(length-2, -1, -1):
            right.append(height[i] if right[-1] < height[i] else right[-1])
        right = right[::-1]
        res = 0
        for i in range(length):
            start = left[i]
            end = right[i]
            area = min(start, end)-height[i]
            res += area
        return res
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = [0]*length
        right = [length-1]*length
        for i in range(length):
            left[i] =  max(height[i], left[i-1]) if i else height[i]
        for i in range(length-1, -1, -1):
            right[i]= max(height[i], right[i+1]) if length-1-i else height[i]
        return sum(min(left[i], right[i])-height[i] for i in range(length))
        
    def trap(self, height: List[int]) -> int:
        stack = list()
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                index = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                right = i
                dis = right-left -1
                area = dis*(min(height[left], height[right]) - height[index])
                res += area
            stack.append(i)
        return res
# @lc code=end

