#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        rows  = len(image)
        cols = len(image[0])
        def dfs(sr:int, sc:int):
            if 0 <= sr < rows and 0<= sc < cols:
                if image[sr][sc] == old_color:
                    image[sr][sc] = newColor
                    dfs(sr, sc+1)
                    dfs(sr, sc-1)
                    dfs(sr+1, sc)
                    dfs(sr-1, sc)
        dfs(sr, sc)
        return image
        
# @lc code=end

