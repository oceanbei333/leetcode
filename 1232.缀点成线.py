#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
from typing import Coroutine


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0] == coordinates[1][0]:
            for port in coordinates[2:]:
                if port[0] != coordinates[0][0]:
                    return False
            return True

        slope = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        for index in range(1, len(coordinates)-1):
            if coordinates[index][0] == coordinates[index+1][0]:
                return False
            if slope != (coordinates[index][1] - coordinates[index+1][1])/(coordinates[index][0]-coordinates[index+1][0]):
                return False
        return True

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        aset = set()
        for index in range(len(coordinates)-1):
            if coordinates[index][0] == coordinates[index+1][0]:
                aset.add(float('inf'))
            else:
                aset.add((coordinates[index][1] - coordinates[index+1][1])/(coordinates[index][0]-coordinates[index+1][0]))
        return len(aset) == 1

# @lc code=end

