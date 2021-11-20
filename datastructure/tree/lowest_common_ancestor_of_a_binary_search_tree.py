# 235 https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Runtime: 76 ms, faster than 77.42% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 18.4 MB, less than 10.54% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        if p.val < root.val:
            if p.val < q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.left, q, p)
        else:
            if p.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return self.lowestCommonAncestor(root.right, q, p)

    """
    Runtime: 76 ms, faster than 77.42% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    Memory Usage: 18.2 MB, less than 78.64% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/64963/3-lines-with-O(1)-space-1-Liners-Alternatives
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root