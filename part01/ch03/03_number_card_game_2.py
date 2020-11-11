n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_val = 100001

    for a in data:
        min_val = min(min_val, a)

    result = max(result, min_val)

print(result)
