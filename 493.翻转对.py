#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        import bisect
        big_nums, count = [], 0
        for num in nums[::-1]:
            # 反向遍历，那么big_nums中的数字的序号都比之后的大
            count += bisect.bisect_left(big_nums, num)
            big_nums.insert(bisect.bisect_left(big_nums, 2*num), 2*num)
        return count

    def reversePairs(self, nums: List[int]) -> int:
        def merge(left: int, mid: int, right: int) -> int:
            sorted_list = []
            i1, i2, count = left, left, 0
            for j in range(mid+1, right+1):
                while i1 <= mid and nums[i1] <= nums[j]:
                    sorted_list.append(nums[i1])
                    i1 += 1
                sorted_list.append(nums[j])
                while i2 <= mid and nums[i2] <= 2*nums[j]:
                    i2 += 1
                count += mid+1-i2
            for i in range(i1, mid+1):
                sorted_list.append(nums[i])
            nums[left: right+1] = sorted_list
            return count

        def mergeSort(left: int, right) -> int:
            if left >= right:
                return 0
            mid = (left+right) >> 1
            return mergeSort(left, mid) + mergeSort(mid+1, right) + merge(left, mid, right)

        return mergeSort(0, len(nums)-1)

    def reversePairs(self, nums: List[int]) -> int:
        def merge(left: int, mid: int, right: int) -> int:
            i, j, count = left, mid+1, 0
            while i <= mid and j <= right:
                if nums[i] > 2*nums[j]:
                    count += mid+1-i
                    j += 1
                else:
                    i += 1
            nums[left: right+1] = sorted(nums[left:right+1])
            return count

        def mergeSort(left: int, right) -> int:
            if left >= right:
                return 0
            mid = (left+right) >> 1
            return mergeSort(left, mid) + mergeSort(mid+1, right) + merge(left, mid, right)

        return mergeSort(0, len(nums)-1)


# @lc code=end
