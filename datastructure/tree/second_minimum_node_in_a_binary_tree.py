# 671 https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 16 ms, faster than 99.87% of Python3 online submissions for Second Minimum Node In a Binary Tree.
    Memory Usage: 14.3 MB, less than 46.11% of Python3 online submissions for Second Minimum Node In a Binary Tree.
    """
    def findSecondMinimumValue(self, root: Optional[TreeNode], m=None) -> int:
        res = [float('inf')]
        def traverse(node):
            if not node:
                return
            if root.val < node.val < res[0]:
                res[0] = node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if res[0] == float('inf') else res[0]

    """
    Runtime: 20 ms, faster than 99.40% of Python3 online submissions for Second Minimum Node In a Binary Tree.
    Memory Usage: 14.4 MB, less than 11.75% of Python3 online submissions for Second Minimum Node In a Binary Tree.
    """
    def findSecondMinimumValue(self, root: Optional[TreeNode], m=None) -> int:
        if not root.left:
            # Single node root
            if m is None:
                return -1

            return root.val

        l = self.findSecondMinimumValue(root.left, root.val if m is None else m)
        r = self.findSecondMinimumValue(root.right, root.val if m is None else m)
        # At root level
        if m is None:
            # single valued tree
            if l == r == root.val:
                return -1
            else:
                m = root.val

        if l == m:
            return r
        elif r == m:
            return l
        else:
            return min(l, r)
