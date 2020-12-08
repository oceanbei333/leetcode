#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        length1 = m
        length2 = n
        length = m+n
        for index in range(length-1, -1, -1):
            if not length2:
                return nums1
            if not length1 or nums1[length1-1] < nums2[length2-1]:
                val = nums2[length2-1]
                length2 -= 1
            else:
                val = nums1[length1 - 1]
                length1 -= 1
            nums1[index] = val
        return nums1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = m+n
        while m and n:
            if nums1[m-1] > nums2[n-1]:
                nums1[length-1] = nums1[m-1]
                m -= 1
            else:
                nums1[length-1] = nums2[n-1]
                n -= 1
            length -= 1
        nums1[:n] = nums2[:n]
        return nums2


# @lc code=end
