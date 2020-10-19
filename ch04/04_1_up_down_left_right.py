n = int(input())
data = input().split()

array = [[0] * n for _ in range(n)]

i = 1
j = 1

for command in data:
    if command == "R" and j < 5:
        j += 1
    elif command == "L" and j > 1:
        j -= 1
    elif command == "U" and i > 1:
        i -= 1
    elif command == "D" and i < 5:
        i += 1
    print(f"{command} : i = {i} / j = {j}")
print(i, ", ", j)
