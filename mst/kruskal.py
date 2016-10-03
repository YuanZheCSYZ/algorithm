# Bring up idea from
# https://github.com/qiwsir/algorithm/blob/master/prim_algorithm.md


from collections import defaultdict
import heapq


def kruskal(graph, n):
    connection, dist = [0] * n, [0] * n
    v_edges = defaultdict(list)
    for i, edges in enumerate(graph):
        for j, w in enumerate(edges):
            if i == j or w is None:
                continue

            v_edges[i].append((w, i, j))

    start_vertex = 0
    candidate_edges = v_edges[start_vertex]
    heapq.heapify(candidate_edges)
    visited = [start_vertex]
    while candidate_edges:
        w, i, j = heapq.heappop(candidate_edges)
        if j not in visited:
            visited.append(j)
            connection[j] = i
            dist[j] = w

            for edge in v_edges[j]:
                if edge[2] not in visited:
                    heapq.heappush(candidate_edges, edge)

    # assert len(visited) == n, "Graph is not fully connected"
    return dist, connection

if __name__ == '__main__':
    _ = None
    graph = [
            [0, 6, 3, _, _, _, _],
            [6, 0, 2, 5, _, _, _],
            [3, 2, 0, 3, 4, _, _],
            [_, 5, 3, 0, 2, 3, _],
            [_, _, 4, 2, 0, 5, _],
            [_, _, _, 3, 5, 0, _],
            [_, _, _, _, _, _, 0],
            ]
    dis, pre = kruskal(graph, len(graph))
    print(dis)
    print(pre)
