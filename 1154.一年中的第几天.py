#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        a_date = datetime.strptime(date, '%Y-%m-%d')
        first_day = a_date.replace(day=1, month=1)
        return (a_date - first_day).days+1

        
# @lc code=end

