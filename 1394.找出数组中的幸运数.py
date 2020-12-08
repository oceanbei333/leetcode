#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        if any(counter[val]==val for val in counter):
            return  int( max(not counter[val]==val or val for val in counter) )
        else:
            return -1
        
# @lc code=end

