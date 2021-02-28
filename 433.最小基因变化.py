#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
from typing import Deque, List, Tuple


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        n = len(start)
        bank_set = set(bank)
        queue = [start]
        aset = {'A', 'C', 'G', 'T'}
        count = 0
        while queue:
            count += 1
            new_queue = []
            for gene in queue:
                for i in range(n):
                    for s in aset-{gene[i]}:
                        new_gene = gene[:i]+s+gene[i+1:]
                        if new_gene == end:
                            return count
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)
                            new_queue.append(new_gene)
            queue = new_queue
        return -1

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        n = len(start)
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        queue = {start}
        back_queue = {end}
        aset = {'A', 'C', 'G', 'T'}
        count = 0
        while queue:
            count += 1
            new_queue = []
            for gene in queue:
                for i in range(n):
                    for s in aset-{gene[i]}:
                        new_gene = gene[:i]+s+gene[i+1:]
                        if new_gene in back_queue:
                            return count
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)
                            new_queue.append(new_gene)
            queue = new_queue
            if len(queue) > len(back_queue):
                queue, back_queue = back_queue, queue
        return -1


# @lc code=end
