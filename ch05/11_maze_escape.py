from collections import deque

n, m = map(int, input().split())

array = []

for _ in range(1, n + 1):
    array.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # print(nx, ny)

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # if array[nx][ny] == 0:
            #     continue

            if not visited[nx][ny] and array[nx][ny] == 1:
                print(nx, ny)
                array[nx][ny] = array[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

            if visited[n - 1][m - 1]:
                break

    return array[n - 1][m - 1]


print(bfs(0, 0))

for i in range(n):
    print(array[i])

# input
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
