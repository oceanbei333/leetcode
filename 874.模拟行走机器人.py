#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        aset = {tuple(point) for point in obstacles}
        aidct = {0:(-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
        di = 1
        x, y = 0, 0
        res = 0
        for command in commands:
            if command == -2:
                di = (di-1)%4
            elif command == -1:
                di = (di+1)%4
            else:
                dx, dy = aidct[di]
                for _ in range(command):
                    if (x+dx, y+dy) not in aset:
                        x += dx
                        y += dy
                        res = max(res, x**2+y**2) 
        return res




        
# @lc code=end

