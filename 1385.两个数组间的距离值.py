#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        aset = set()
        for num in arr2:
            aset |= set(range(num-d, num+d+1))
        return sum(not num in aset for num in arr1)
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for x in arr1:
            p = bisect.bisect_left(arr2, x)
            if p == len(arr2) or abs(arr2[p]-x) >d:
                if not p or abs(arr2[p-1] -x) >d:
                    count += 1
        return count

# @lc code=end

