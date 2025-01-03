"""
https://leetcode.com/problem-list/binary-tree/?difficulty=MEDIUM
URL: https://leetcode.com/problems/delete-node-in-a-bst/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_larger_node = self.findMin(root.right)
            root.val = min_larger_node.val

            root.right = self.deleteNode(root.right, min_larger_node.val)

        return root

    def findMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
