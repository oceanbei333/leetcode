#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        from collections import defaultdict
        adict = defaultdict(int)
        def dfs(root:TreeNode):
            if not root:
                return
            adict[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if not adict:
            return []
        max_c = max(adict.values())
        return [val for val, count in adict.items() if count == max_c]
        
    def findMode(self, root: TreeNode) -> List[int]:
        alist  = []
        base = None
        max_n = 0
        count = 0
        def update(val:int):
            nonlocal max_n
            nonlocal base
            nonlocal count
            nonlocal alist
            if base == val:
                count += 1
            else:
                base = val
                count = 1
            if count == max_n:
                alist.append(val)
            elif count > max_n:
                alist = [base]
                max_n = count


        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            update(root.val)
            dfs(root.right)
        dfs(root)
        return alist

# @lc code=end

