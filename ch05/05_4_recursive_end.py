def recursive_function(i):
    if i == 100:
        return
    print(i, f'번째 함수에서 {i + 1} 번째 재쉬 함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번째 함수를 종료합니다.')


recursive_function(1)
