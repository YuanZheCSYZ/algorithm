# 530 https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Runtime: 44 ms, faster than 89.22% of Python online submissions for Minimum Absolute Difference in BST.
    Memory Usage: 17.5 MB, less than 46.12% of Python online submissions for Minimum Absolute Difference in BST.
    """
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findMin(root)[-1]

    def findMin(self, root):
        res = [root.val, root.val, 1000000]
        if not root.left and not root.right:
            return res

        if root.left:
            tmp = self.findMin(root.left)
            res = [tmp[0], root.val, min(tmp[2], root.val - tmp[1])]

        if root.right:
            res_r = self.findMin(root.right)
            res = [res[0], res_r[1], min(res[2], res_r[2], res_r[0] - root.val)]

        return res
