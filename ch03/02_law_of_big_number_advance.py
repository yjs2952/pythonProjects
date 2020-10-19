# 임의의 배열에 주어진 수들을 m 번 더하여 가장 큰 수를 만든다.
# 배열의 특정 인덱스에 해당하는 수가 연속해서 k번을 초과할 수 없다.

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

first_largest_number = data[0]
second_largest_number = data[1]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first_largest_number
result += (m - count) * second_largest_number

print(result)
