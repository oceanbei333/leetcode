#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_logs = []
        letter_logs = []
        for log in logs:
            log_list = log.split(' ')
            if log_list[1].isalpha():
                letter_logs.append(log_list)
            else:
                num_logs.append(log)
        letter_logs.sort(key=lambda x: (x[1:], x[0]))
        letter_logs = [' '.join(log) for log in letter_logs]
        return letter_logs + num_logs
        
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def func(log: str):
            id_, rest = log.split(' ', 1)
            return (0, rest , id_ ) if rest[0].isalpha() else (1, )
        logs.sort(key=func)
        return logs

# @lc code=end

