#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for index in range(len(arr)-1):
            if arr[index]>arr[index+1]:
                return index
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low = 1
        high = len(arr)-2
        while low <= high:
            mid = (low+high)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]>arr[mid+1]:
                high = mid -1
            else:
                low = mid+1


# @lc code=end

