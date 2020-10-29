from collections import deque


def bfs(graph, i, visited):
    queue = deque([i])
    visited[i] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for num in graph[node]:
            if not visited[num]:
                queue.append(num)
                visited[num] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
