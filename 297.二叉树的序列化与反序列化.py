#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        queue = deque([root])
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    res.append(str( node.val ))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append('#')
        return ':'.join(res)
        
        

    def deserialize(self, data:str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        node_list = data.split(':')[::-1]
        if node_list[-1] == '#':
            return 
        root = TreeNode(node_list.pop())
        queue = deque([root])
        while node_list:
            parent = queue.popleft()
            left = node_list.pop()
            right = node_list.pop()
            if left != '#':
                parent.left = TreeNode(int(left))
                queue.append(parent.left)
            if right != '#':
                parent.right = TreeNode(int(right))
                queue.append(parent.right)
        return root
        
    def serialize(self, root):
        res = []
        def dfs(root):
            if not root:
                res.append('#')
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ':'.join(res)

    def deserialize(self, data:str):
        nodes = data.split(':')[::-1]
        def dfs():
            node = nodes.pop()
            if node == '#':
                return
            root = TreeNode(int(node))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
    def deserialize(self, data:str):
        nodes = iter(data.split(':'))
        def dfs():
            node = next(nodes)
            if node == '#':
                return
            root = TreeNode(int(node))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
    def serialize(self, root):
        res = []
        def dfs(root):
            if not root:
                res.append('#')
                return
            dfs(root.left)
            dfs(root.right)
            res.append(str(root.val))
        dfs(root)
        return ':'.join(res)

    def deserialize(self, data:str):
        nodes = data.split(':')
        def dfs():
            node = nodes.pop()
            if node == '#':
                return
            root = TreeNode(int(node))
            root.right = dfs()
            root.left = dfs()
            return root
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

