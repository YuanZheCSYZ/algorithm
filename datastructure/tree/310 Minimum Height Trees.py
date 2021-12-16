# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    """
    Runtime: 1300 ms, faster than 5.09% of Python3 online submissions for Minimum Height Trees.
    Memory Usage: 119 MB, less than 5.04% of Python3 online submissions for Minimum Height Trees.

    The answer should be the mid of the longest path.

    The longest path from any point is part of the longest path and the leave node on the other side is the beginning
    of the longest path. Hence a second dfs/bfs from this path will return the longest path.
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [x for x in range(n)]

        edge_map = collections.defaultdict(list)
        for x, y in edges:
            edge_map[x].append(y)
            edge_map[y].append(x)

        t = self.findMaxLength(n, edge_map, [edges[0][0]])
        t = self.findMaxLength(n, edge_map, [t[-1]])
        l = len(t)
        if l % 2:
            return [t[l // 2]]
        else:
            return [t[l // 2 - 1], t[l // 2]]

    def findMaxLength(self, n, edge_map, nodes):
        if len(nodes) == n:
            return nodes

        node = nodes[-1]
        res1 = nodes
        for end in edge_map[node]:
            if end not in nodes:
                tmp = self.findMaxLength(n, edge_map, nodes + [end])
                if len(res1) < len(tmp):
                    res1 = tmp

        return res1

    """
    Runtime: 240 ms, faster than 59.54% of Python3 online submissions for Minimum Height Trees.
    Memory Usage: 18.8 MB, less than 58.10% of Python3 online submissions for Minimum Height Trees.
    https://leetcode.com/problems/minimum-height-trees/discuss/923055/Python-O(n)-by-leave-node-removal-w-Visualization
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        total_node_count = n

        if total_node_count == 1:
            # Quick response for one node tree
            return [0]

        # build adjacency matrix
        adj_matrix = defaultdict(set)

        for src_node, dst_node in edges:
            adj_matrix[src_node].add(dst_node)
            adj_matrix[dst_node].add(src_node)

        # get leaves node whose degree is 1
        leave_nodes = [node for node in adj_matrix if len(adj_matrix[node]) == 1]

        # keep doing leave nodes removal until total node count is smaller or equal to 2
        while total_node_count > 2:

            total_node_count -= len(leave_nodes)

            leave_nodes_next_round = []

            # leave nodes removal
            for leaf in leave_nodes:

                neighbor = adj_matrix[leaf].pop()
                adj_matrix[neighbor].remove(leaf)

                if len(adj_matrix[neighbor]) == 1:
                    leave_nodes_next_round.append(neighbor)

            leave_nodes = leave_nodes_next_round

        # final leave nodes are root node of minimum height trees
        return leave_nodes
