#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] 重复至少 K 次且长度为 M 的模式
#

# @lc code=start
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)-m*k+1):
            for index in range(k-1):
                start = i+index*m
                if arr[start: start+m] != arr[start+m:start+2*m]:
                    break
            else:
                return True
        return False

# @lc code=end

