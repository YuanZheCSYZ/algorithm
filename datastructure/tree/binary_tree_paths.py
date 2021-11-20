# 257 https://leetcode.com/problems/binary-tree-paths/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 28 ms, faster than 90.84% of Python3 online submissions for Binary Tree Paths.
    Memory Usage: 14.4 MB, less than 31.14% of Python3 online submissions for Binary Tree Paths.
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        result = []
        if root.left:
            result += ["{}->{}".format(root.val, path) for path in self.binaryTreePaths(root.left)]
        if root.right:
            result += ["{}->{}".format(root.val, path) for path in self.binaryTreePaths(root.right)]

        return result

    """
    Runtime: 28 ms, faster than 90.84% of Python3 online submissions for Binary Tree Paths.
    Memory Usage: 14.3 MB, less than 62.06% of Python3 online submissions for Binary Tree Paths.
    https://leetcode.com/problems/binary-tree-paths/discuss/68272/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively).
    """
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
        return res