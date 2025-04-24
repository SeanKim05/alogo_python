from collections import deque

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# def bfs_queue(g, start):
#     visited = [start]
#     q = deque([start])
#
#     while q:
#         node = q.popleft()
#         for adj in g[node]:
#             if adj not in visited:
#                 q.append(adj)
#                 visited.append(adj)
#
#     return visited

def bfs_queue(g, start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in g[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

assert bfs_queue(graph, 1) == [1, 2, 5, 9, 3, 6, 8, 10, 4, 7]

def bfs(g, start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in g[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)


