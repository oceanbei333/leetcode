#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

'''

'''

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        length1 = len(nums1)
        length2 = len(nums2)
        totalleft = (length1+length2+1)//2
        left = 0
        right = length1
        # 二分查找
        while left < right:
            # mid != 0
            mid = (left + right+1)//2
            if nums1[mid-1] > nums2[totalleft-mid]:
                right = mid-1
            else:
                left = mid

        # 最终left == right
        i = left
        j = totalleft - i
        # i ,i-1, j, j-1  out of range
        nums1LeftMax = nums1[i-1] if i else float('-inf')
        nums1RightMin = nums1[i] if i - length1 else float('inf')
        nums2LeftMax = nums2[j-1] if j else float('-inf')
        nums2RightMin = nums2[j] if j - length2 else float('inf')

        if (length1+length2) % 2:
            return max(nums1LeftMax, nums2LeftMax)
        else:
            return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin))/2


class Solution:
    def helper(self, nums1: List[int], nums2: List[int], k: int) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1  # 保持nums1比较长
        if not len(nums2):
            return nums1[k-1]  # 短数组空，直接返回
        #  不能找最0小的数
        if k == 1:
            return min(nums1[0], nums2[0])  # 找最小数，比较数组首位
        t = min(k//2, len(nums2))  # 保证不上溢
        # 因为是整除2，所有最终的结果只可能是这个位置或者以后的位置，所以，抛弃小的那一部分
        if nums1[t-1] >= nums2[t-1]:
            return self.helper(nums1, nums2[t:], k-t)
        else:
            return self.helper(nums1[t:], nums2, k-t)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2
        return (self.helper(nums1, nums2, k1) + self.helper(nums1, nums2, k2)) / 2


# @lc code=end
