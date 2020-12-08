#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root:TreeNode, s:str) -> int:
            if not root:
                return 0
            s += str(root.val)
            if not root.left and not root.right:
                return int(s, 2)
            return dfs(root.left, s) + dfs(root.right, s)
        return dfs(root, '0b')

    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, str(root.val))]
        res = 0
        while stack:
            node, val = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += int('0b'+ val, 2)
                if node.left:
                    stack.append(( node.left, val+str(node.left.val) ))
                if node.right:
                    stack.append(( node.right, val+str(node.right.val) ))
        return res


        
# @lc code=end

