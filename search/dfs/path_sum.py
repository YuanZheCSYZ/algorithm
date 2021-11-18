# 112 https://leetcode.com/problems/path-sum/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 44 ms, faster than 65.05% of Python3 online submissions for Path Sum.
    Memory Usage: 15.1 MB, less than 77.54% of Python3 online submissions for Path Sum.
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        remaining = targetSum - root.val
        if remaining == 0 and not root.left and not root.right:
            return True

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

    """
    Runtime: 32 ms, faster than 98.83% of Python3 online submissions for Path Sum.
    Memory Usage: 15 MB, less than 77.54% of Python3 online submissions for Path Sum.
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            remaining = targetSum - root.val
            if remaining == 0 and not root.left and not root.right:
                return True

            return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)

        return False

    """
    Runtime: 28 ms, faster than 99.80% of Python3 online submissions for Path Sum.
    Memory Usage: 15.1 MB, less than 43.96% of Python3 online submissions for Path Sum.
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            targetSum -= root.val
            if targetSum == 0 and (not root.left and not root.right):
                return True

            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        return False
