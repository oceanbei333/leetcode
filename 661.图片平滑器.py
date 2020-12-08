#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        length1 = len(M)
        length2 = len(M[0])
        result = [[0]*length2 for _ in range(length1)]
        for i in range(length1):
            for j in range(length2):
                count = 0
                num = 0
                for m in range(-1, 2):
                    for n in range(-1, 2):
                        if -1 < i+m < length1 and -1 < j+n < length2:
                            count += 1
                            num += M[i+m][j+n]
                result[i][j] = num//count
        return result

# @lc code=end
