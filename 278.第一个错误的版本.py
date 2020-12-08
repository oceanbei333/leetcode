#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        low = 2
        high = n
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid -1
            else:
                low = mid+1
        return  low


        
# @lc code=end

