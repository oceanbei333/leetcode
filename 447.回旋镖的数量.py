#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
from collections import Counter
from scipy.special import perm

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for point in points:
            
            # distance2 记录对这个点来说的所有的距离
            distance2 = []
            for neighbor in points:
                distance2.append((point[0] - neighbor[0]) ** 2 + (point[1] - neighbor[1]) ** 2)
            
            frequency = Counter(distance2)
            
            for dist,num in frequency.items():
                if num >= 2:
                    count += perm(num,2)
                    
        return int(count)

# @lc code=end

