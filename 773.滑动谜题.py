#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        target, step, visited = '123450', 0, set()
        queue = {''.join(str(num) for row in board for num in row)}
        while queue:
            visited |= queue
            new_queue = set()
            for word in queue:
                if word == target:
                    return step
                zero = word.index('0')
                for next_ in moves[zero]:
                    alist = list(word)
                    alist[zero], alist[next_] = alist[next_], alist[zero]
                    new_word = ''.join(alist)
                    if new_word not in visited:
                        new_queue.add(new_word)
            queue = new_queue
            step += 1
        return -1

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))
        target, step, visited = '123450', 0, set()
        front = {''.join(str(num) for row in board for num in row)}
        back = {target}
        while front:
            visited |= front
            new_queue = set()
            for word in front:
                zero = word.index('0')
                for next_ in moves[zero]:
                    alist = list(word)
                    alist[zero], alist[next_] = alist[next_], alist[zero]
                    new_word = ''.join(alist)
                    if word in back:
                        return step
                    if new_word not in visited:
                        new_queue.add(new_word)
            front = new_queue
            step += 1
            if len(front) > len(back):
                front, back = back, front
        return -1


# @lc code=end
