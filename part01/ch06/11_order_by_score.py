n = int(input())

array = []

for i in range(n):
    arr_input = input().split()
    array.append((arr_input[0], int(arr_input[1])))

array.sort(key=lambda data: data[1])

for student in array:
    print(student[0], end=' ')
