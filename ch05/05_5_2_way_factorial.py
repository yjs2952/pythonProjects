def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
        print(i)
        print(result)
    return result


def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print(f'반복적 구현 : {factorial_iterative(5)}')
print(f'재귀적 구현 : {factorial_recursive(5)}')
