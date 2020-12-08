#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        adict = {emp.id: emp for emp in employees}
        def get_imp(id: int)->int:
            return sum(get_imp(id_) for id_ in adict[id].subordinates  ) + adict[id].importance
        return get_imp(id)
        
# @lc code=end

