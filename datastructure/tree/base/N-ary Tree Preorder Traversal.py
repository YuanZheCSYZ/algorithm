# https://leetcode.com/problems/n-ary-tree-preorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        pending = [root]
        res = []
        while pending:
            x = pending.pop()
            res.append(x.val)
            if x.children:
                pending += x.children[::-1]

        return res
