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
        front = [start]
        aset = {'A', 'C', 'G', 'T'}
        count = 0
        while front:
            count += 1
            new_front = []
            for gene in front:
                for i in range(n):
                    for s in aset-{gene[i]}:
                        new_gene = gene[:i]+s+gene[i+1:]
                        if new_gene == end:
                            return count
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)
                            new_front.append(new_gene)
            front = new_front
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        n = len(start)
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        front = {start}
        back = {end}
        aset = {'A', 'C', 'G', 'T'}
        count = 0
        while front:
            count += 1
            new_front = []
            for gene in front:
                for i in range(n):
                    for s in aset-{gene[i]}:
                        new_gene = gene[:i]+s+gene[i+1:]
                        if new_gene in back:
                            return count
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)
                            new_front.append(new_gene)
            front = new_front
            if len(front) > len(back):
                front, back = back, front
        return -1


# @lc code=end
