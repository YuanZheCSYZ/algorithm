# 653 https://leetcode.com/problems/two-sum-iv-input-is-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 80 ms, faster than 73.53% of Python3 online submissions for Two Sum IV - Input is a BST.
    Memory Usage: 16.6 MB, less than 75.20% of Python3 online submissions for Two Sum IV - Input is a BST.
    """
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        unvisited = [root]
        mapping = set()
        while unvisited:
            p = unvisited.pop()
            remaining = k - p.val
            if remaining in mapping:
                return True
            else:
                mapping.add(p.val)

            if p.left:
                unvisited.append(p.left)
            if p.right:
                unvisited.append(p.right)
