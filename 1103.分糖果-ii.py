#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        i = 1
        while candies:
            index = i%num_people-1
            if candies >= i:
                res[index] += i
                candies -= i
            else:
                res[index] += candies
                candies = 0
            i += 1
        return res

        
# @lc code=end

