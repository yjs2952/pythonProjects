import time


def binary_search_length(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        result = sum_after_cut(array, mid)
        # print(f"target = {target}, mid = {mid}, result = {result}")
        if result == target:
            return mid

        if result < target:
            end = mid + 1

        if result > target:
            start = mid - 1
    return None


def sum_after_cut(array, length):
    result = 0
    for i in range(n - 1, -1, -1):
        if array[i] > length:
            result += (array[i] - length)
        else:
            break
    return result


n, m = map(int, input().split())
array = list(map(int, input().split()))

start_time = time.time()
array = sorted(array)
max_length = array[-1]

print(binary_search_length(array, m, 0, max_length))
end_time = time.time()

print(f"time = {end_time - start_time}")

