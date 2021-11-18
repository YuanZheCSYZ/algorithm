# 111 https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Runtime: 504 ms, faster than 76.70% of Python3 online submissions for Minimum Depth of Binary Tree.
    Memory Usage: 50 MB, less than 63.12% of Python3 online submissions for Minimum Depth of Binary Tree.
    DFS
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 1, 0)

    def dfs(self, root, current_depth, min_depth):
        if not root:
            return min_depth

        if min_depth and min_depth <= current_depth:
            return min_depth

        if not root.left and not root.right:
            return current_depth

        left_min = self.dfs(root.left, current_depth + 1, min_depth)
        if not min_depth:
            min_depth = left_min
        else:
            min_depth = min(min_depth, left_min)

        return self.dfs(root.right, current_depth + 1, min_depth)

    """
    Runtime: 472 ms, faster than 90.43% of Python3 online submissions for Minimum Depth of Binary Tree.
    Memory Usage: 49.1 MB, less than 85.98% of Python3 online submissions for Minimum Depth of Binary Tree.
    BFS
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth

        queue = [root]

        while queue:
            depth += 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return 0