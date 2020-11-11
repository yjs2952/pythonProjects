n, k = map(int, input().split())

array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

# for i in range(k):
#     min_A = min(array_A)
#     max_B = max(array_B)
#
#     if min_A < max_B:
#         array_B[array_B.index(max_B)], array_A[array_A.index(min_A)] \
#             = array_A[array_A.index(min_A)], array_B[array_B.index(max_B)]
#     else:
#         break

array_A.sort()
array_B.sort(reverse=True)

for i in range(k):
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else:
        break

print(sum(array_A))
