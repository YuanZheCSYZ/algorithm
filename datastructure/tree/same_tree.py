# 100 https://leetcode.com/problems/same-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 32 ms, faster than 65.62% of Python3 online submissions for Same Tree.
    Memory Usage: 14.2 MB, less than 87.06% of Python3 online submissions for Same Tree.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
