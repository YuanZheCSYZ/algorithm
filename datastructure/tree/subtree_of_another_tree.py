# 572 https://leetcode.com/problems/subtree-of-another-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 93 ms, faster than 92.06% of Python3 online submissions for Subtree of Another Tree.
    Memory Usage: 15.2 MB, less than 63.75% of Python3 online submissions for Subtree of Another Tree.
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return (not root) == (not subRoot)

        if root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right,
                                                                                                    subRoot.right):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, root, subRoot):
        if not root or not subRoot:
            return (not root) == (not subRoot)

        return root.val == subRoot.val and self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right,
                                                                                                      subRoot.right)
