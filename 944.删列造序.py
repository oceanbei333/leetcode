#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(sorted(letters)!=list(letters) for letters in zip(*A))
# @lc code=end

