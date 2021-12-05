# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    """
    Runtime: 44 ms, faster than 95.27% of Python3 online submissions for N-ary Tree Postorder Traversal.
    Memory Usage: 16.1 MB, less than 27.43% of Python3 online submissions for N-ary Tree Postorder Traversal.
    """
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        pending = [root]
        while pending:
            curr = pending.pop()
            res.append(curr.val)
            pending.extend(curr.children)

        return res[::-1]

    """
    Runtime: 40 ms, faster than 98.80% of Python3 online submissions for N-ary Tree Postorder Traversal.
    Memory Usage: 16.2 MB, less than 27.43% of Python3 online submissions for N-ary Tree Postorder Traversal.
    """
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)

        recursion(root, res)
        return res
