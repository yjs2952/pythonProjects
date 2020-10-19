n, k = map(int, input().split())

result = 0

while n != 1:
    if n % k != 0:
        n = n - 1
        print("n 에서 1 빼기")
    else:
        n = n // k
        print("n을 k로 나누기")
    result += 1

print(result)
