#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counter = Counter(tasks)
        res = 0
        while 1:
            i = len(counter)
            for task, num in counter.most_common(n+1):
                if num == 1:
                    counter.pop(task)
                else:
                    counter[task] -= 1
            if not counter:
                return res + i
            res += n+1

    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        counter = Counter(tasks)
        max_ = max(counter.values())
        max_n = 0
        for num in counter.values():
            if num == max_:
                max_n += 1
        res = (max_-1)*(n+1) + max_n
        return res if res >= len(tasks) else len(tasks)


# @lc code=end
