import time


def binary_search_length(array, target, start, end):
    global result
    while start <= end:
        mid = (start + end) // 2
        total = sum_after_cut(array, mid)
        print(f"target = {target}, mid = {mid}, total = {total}")

        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


def sum_after_cut(array, length):
    total = 0
    for i in range(n - 1, -1, -1):
        if array[i] > length:
            total += (array[i] - length)
    return total


n, m = map(int, input().split())
array = list(map(int, input().split()))

start_time = time.time()
max_length = max(array)
result = 0

print(binary_search_length(array, m, 0, max_length))
end_time = time.time()
print(f"time = {end_time - start_time}")
