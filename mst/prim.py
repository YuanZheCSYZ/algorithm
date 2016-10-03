def prim(graph, n):
    connection, dist = [0] * n, graph[0]
    visited = [True] + [False]*(n-1)

    for _ in range(n-1):
        _min = None
        j = 0
        for i in range(1, n):
            if not visited[i] and dist[i] and (_min is None or _min > dist[i]):
                _min = dist[i]
                j = i

        assert _min is not None, "Graph is not fully connected"
        visited[j] = True
        for i in range(1, n):
            if not visited[i] and graph[j][i] and (
                    not dist[i] or dist[i] > graph[j][i]):
                dist[i] = graph[j][i]
                connection[i] = j

    return connection, dist


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
    dis, pre = prim(graph, len(graph))
    print(dis)
    print(pre)
