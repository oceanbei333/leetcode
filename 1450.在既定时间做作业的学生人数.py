#
# @lc app=leetcode.cn id=1450 lang=python3
#
# [1450] 在既定时间做作业的学生人数
#

# @lc code=start
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum( start_time<= queryTime<=end_time for start_time, end_time in zip(startTime, endTime))
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum( startTime[index]<= queryTime<=endTime[index] for index in range(len(startTime)))
# @lc code=end

