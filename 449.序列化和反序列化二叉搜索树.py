#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ''
        res = str(root.val)
        left = self.serialize(root.left)
        if left:
            res += '-' + left
        right = self.serialize(root.right)
        if right:
            res += '-' + right
        return res

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        alist = [int(val) for val in data.split('-') if val]

        def helper(alist):
            if not alist:
                return
            root = TreeNode(alist[0])
            i = 1
            while i < len(alist) and alist[i] < root.val:
                i += 1
            root.left = helper(alist[1:i])
            root.right = helper(alist[i:])
            return root
        return helper(alist)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end
