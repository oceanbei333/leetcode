#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        alist = []
        while head:
            alist.append(head)
            head = head.next

        def helper(alist):
            if not alist:
                return
            mid = len(alist)//2
            root = TreeNode(alist[mid].val)
            root.left = helper(alist[0:mid])
            root.right = helper(alist[mid+1:])
            return root
        return helper(alist)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def _sortedListToBST(head, tail_next):
            if head is tail_next:
                return
            mid = fast = head
            while fast is not tail_next and fast.next is not tail_next:
                mid = mid.next
                fast = fast.next.next
            root = TreeNode(mid.val)
            root.left = _sortedListToBST(head, mid)
            root.right = _sortedListToBST(mid.next, tail_next)
            return root
        return _sortedListToBST(head, None)

# @lc code=end
