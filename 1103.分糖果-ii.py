#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        index = 0
        while candies:
            print(candies)
            print(res)
            if index >= num_people:
                index = 0
            if candies > index+1:
                res[index] += index+1
                candies -= index+1
            else:
                res[index] = candies
                candies = 0
            index+=1
        return res
        
# @lc code=end

