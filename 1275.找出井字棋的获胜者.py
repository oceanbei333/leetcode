#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) <5:
            return "Pending"
        alist = [[None]*3 for _ in range(3)]
        is_A = False
        for i, j in moves:
            is_A = not is_A
            alist[i][j] = is_A
        if is_A == alist[0][0] == alist[1][1]== alist[2][2]:
            return 'A' if is_A else 'B'
        elif is_A == alist[0][2] == alist[1][1]== alist[2][0]:
            return 'A' if is_A else 'B'
        elif any(alist[i][0]==alist[i][1]==alist[i][2]==is_A for i in range(3)):
            return 'A' if is_A else 'B'
        elif any(alist[0][i]==alist[1][i]==alist[2][i]==is_A for i in range(3)):
            return 'A' if is_A else 'B'
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

        
        


        
# @lc code=end

