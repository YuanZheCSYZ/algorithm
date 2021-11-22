# 543 https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Runtime: 28 ms, faster than 93.19% of Python online submissions for Diameter of Binary Tree.
    Memory Usage: 16.5 MB, less than 10.73% of Python online submissions for Diameter of Binary Tree.
    """
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findLongest(root)[-1]

    def findLongest(self, root):
        # deepest, longest
        res = [0, 0]
        if not root or not root.left and not root.right:
            return res

        if root.left:
            res = self.findLongest(root.left)
            res[0] += 1
            res[1] = max(res[0], res[1])

        if root.right:
            tmp = self.findLongest(root.right)
            res[1] = max(tmp[1], res[1], res[0] + tmp[0] + 1)
            res[0] = max(res[0], tmp[0] + 1)

        return res
