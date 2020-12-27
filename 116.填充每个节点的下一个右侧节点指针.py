#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = [root]
        while queue:
            new_queue = []
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return root

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        first = root
        while first.left:
            head = first
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            first = first.left
        return root
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        head = root
        while head and head.next:
            head.right.next = head.next.left
            head = head.next
        self.connect(root.left)
        self.connect(root.right)
        return root


# @lc code=end
