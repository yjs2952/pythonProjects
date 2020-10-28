def dfs(graph, i, visited):
    stack = [i]
    print(i, end=' ')
    while stack:

        node = stack[-1]
        visited[node] = True
        # flag = False

        for num in graph[node]:
            if not visited[num]:
                stack.append(num)
                visited[num] = True
                # flag = True
                print(num, end=' ')
                break

            if num == graph[node][-1]:
                stack.pop()

        # if not flag:
        #     stack.pop()

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

dfs(graph, 1, visited)
