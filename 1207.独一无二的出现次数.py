#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr).values()
        return len(set(counter)) == len(tuple(counter))

        
# @lc code=end

