# 94 https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 28 ms, faster than 86.48% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 14.1 MB, less than 76.64% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        unvisited = []
        if root:
            if root.right:
                unvisited.append(root.right)
                root.right = None

            unvisited.append(root)
            if root.left:
                unvisited.append(root.left)
                root.left = None

        while unvisited:
            p = unvisited.pop()
            if p.right:
                unvisited.append(p.right)
                p.right = None

            if p.left:
                unvisited.append(p)
                unvisited.append(p.left)
                p.left = None
            else:
                result.append(p.val)

        return result

    """
    Runtime: 28 ms, faster than 86.48% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 14 MB, less than 92.11% of Python3 online submissions for Binary Tree Inorder Traversal.
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while root or stack:
            if root is None:
                root = stack.pop()
                res.append(root.val)
                root = root.right
            else:
                stack.append(root)
                root = root.left

        return res
