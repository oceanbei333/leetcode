#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten_n = 0
        five_n = 0
        for val in bills:
            if val == 5:
                five_n += 1
            elif val == 10:
                if five_n:
                    five_n -= 1
                    ten_n += 1
                else:
                    return False
            elif val == 20:
                if ten_n:
                    if five_n:
                        five_n -= 1
                    else:
                        return False
                    ten_n -= 1
                elif five_n >=3:
                    five_n -= 3
                else:
                    return False
        return True
        
# @lc code=end

