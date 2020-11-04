n = int(input())
parts = list(map(int, input().split()))

m = int(input())
need_parts = list(map(int, input().split()))

parts = sorted(parts)


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return 'yes'
        elif target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'


for i in range(m):
    print(binary_search(parts, need_parts[i], 0, n - 1), end=' ')

