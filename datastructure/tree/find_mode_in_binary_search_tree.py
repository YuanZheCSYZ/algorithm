# 501 https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    """
    Runtime: 109 ms, faster than 14.15% of Python online submissions for Find Mode in Binary Search Tree.
    Memory Usage: 21.3 MB, less than 49.52% of Python online submissions for Find Mode in Binary Search Tree.
    """
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        mapping = collections.defaultdict(int)
        g_max = 0
        unvisited = [root]
        while unvisited:
            p = unvisited.pop()
            if not p:
                continue

            mapping[p.val] += 1
            if g_max < mapping[p.val]:
                g_max = mapping[p.val]

            if p.left:
                unvisited.append(p.left)
            if p.right:
                unvisited.append(p.right)

        return [key for key, value in mapping.items() if value == g_max]

    """
    Runtime: 36 ms, faster than 99.68% of Python online submissions for Find Mode in Binary Search Tree.
    Memory Usage: 17.5 MB, less than 100.00% of Python online submissions for Find Mode in Binary Search Tree.
    """
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        g_max = 0
        max_values = set()
        current_cnt = -1
        current_value = None
        unvisited = [root]
        while unvisited:
            p = unvisited.pop()
            if p.right or p.left:
                if p.right:
                    unvisited.append(p.right)
                    p.right = None

                unvisited.append(p)
                if p.left:
                    unvisited.append(p.left)
                    p.left = None
            else:
                if current_value != p.val:
                    current_cnt = 1
                    current_value = p.val
                else:
                    current_cnt += 1

                if g_max < current_cnt:
                    g_max = current_cnt
                    max_values = {current_value}
                elif g_max == current_cnt:
                    max_values.add(current_value)

        return max_values
