n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input())))

visited = [[False] * m for i in range(n)]


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 0
    if not visited[x][y] and array[x][y] == 0:
        visited[x][y] = True

        return dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1) + 1

    return 0


count = 0

for i in range(n):
    for j in range(m):
        result = dfs(i, j)
        if result > 0:
            print(result)
            count += 1

print(count)
