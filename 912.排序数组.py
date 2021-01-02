#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        def BubbleSort(nums):
            n = len(nums)
            index = 0
            for _ in range(n):
                flag = False
                for i in range(index, n-1):
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                        flag = True
                if not flag:
                    break
            return nums
        return BubbleSort(nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        def InsertSort():
            n = len(nums)
            for i in range(1, n):
                for j in range(i-1, -1, -1):
                    if nums[j] > nums[j+1]:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
            return nums
        return InsertSort()

    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(list1: list, list2: list):
            res = []
            while list1 and list2:
                if list1[-1] > list2[-1]:
                    res.append(list1.pop())
                else:
                    res.append(list2.pop())
            return list1 or list2 + res[::-1]

        def MergeSort(nums):
            n = len(nums)
            if n <= 1:
                return nums
            mid = n >> 1
            return merge(MergeSort(nums[:mid]), MergeSort(nums[mid:]))
        return MergeSort(nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        def SelectSort():
            n = len(nums)
            for i in range(n):
                min_val = min(nums[i:])
                min_index = nums[i:].index(min_val) + i
                nums[i], nums[min_index] = nums[min_index], nums[i]
            return nums
        return SelectSort()

    def sortArray(self, nums: List[int]) -> List[int]:
        def QuickSort(low: int, high: int):
            if low > high:
                return
            pivot = high
            i = low
            for j in range(low, high):
                if nums[j] <= nums[pivot]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[pivot] = nums[pivot], nums[i]
            QuickSort(low, i-1)
            QuickSort(i+1, high)
        QuickSort(0, len(nums)-1)
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        def CountingSort():
            from collections import Counter
            counter = Counter(nums)
            res = []
            for num in sorted(counter.keys()):
                res.extend([num]*counter[num])
            return res
        return CountingSort()

    def sortArray(self, nums: List[int]) -> List[int]:
        from heapq import heappush, heappop
        heap = []
        for num in nums:
            heappush(heap, num)
        return [heappop(heap) for _ in range(len(nums))]

    def sortArray(self, nums: List[int]) -> List[int]:
        import bisect
        res = []
        for num in nums:
            bisect.insort(res, num)
        return res


# @lc code=end
