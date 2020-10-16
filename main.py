# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = 100
print(a)

a = -.8
print(a)

a = -8.
print(a)

a = 1e9
print(a)

a = 0.3 + 0.6
print(a)

a = 0.3 + 0.6
if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

a = 7
b = 3

print(a / b)
print(a % b)
print(a // b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[1:5])

print(a[0])

a = []
print("a : ", a)

array = [i for i in range(20) if i % 2 == 1]
print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)

print(array)

array = [i * i for i in range(1, 10)]

print(array)

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

a = [1, 4, 3]
print("기본리스트: ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입 : ", a)

# 오름차순 정렬
a.sort()
print("오름차순 정렬 : ", a)

# 내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬 : ", a)

a.reverse()
print("원소 뒤집기 : ", a)

print("값이 3인 데이터 개수 : ", a.count(3))

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

data = 'hello world'
print(data)

data = "don't you know \"Python\"?"
print(data)

a = "hello"
b = 'world'
print(a + " " + b)

a = "String"
print(a * 3)

print("""Life is too short,
You need python""")

a = "ABCDEF"
print(a[2:4])

a = (1, 2, 3, 4)
print(a)

# a[2] = 7

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 담은 리스트
key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

print(a | b)
print(a & b)
print(a - b)

data = {1, 2, 3}
print(data)

data.add(4)
print(data)

data.update([5, 6])
print(data)

data.remove(3)
print(data)

x = 15

if x > 10:
    print(x)

score = 85

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print('학점 : B')
else:
    print("퇴학")

score = 69

if score >= 70:
    print('70')
    if score >= 90:
        print("좀 하네?")
else:
    print("70 미만")
    print("허접")

print(10 == 9)

score = 85

if score >= 80:
    pass
else:
    print('80 미만')

print('fin')

if score >= 80:
    result = "succsess"
else:
    result = "fail"

print(result)

result = "success" if score >= 80 else "fail"

print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]
result = [i for i in a if i not in remove_set]

print(result)

i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

result = 0

for i in range(1, 2):
    result += i

print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 합격")

cheating_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다")

for i in range(2, 10):
    for j in range(1, 10):
        print(i, " X ", j, " = ", i * j)


def add(a1, a2):
    return a1 + a2


print(add(3, 7))

a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)


def add(a, b):
    return a + b


print(add(3, 7))

print((lambda a, b: a + b)(3, 7))

# n = int(input())
#
# data = list(map(int, input().split()))

# data.sort(reverse=True)
# print(data)

# q, m, k = map(int, input().split())

# print(q, m, k)

# import sys
#
# data = sys.stdin.readline().rstrip()
# print(data)

a = 1
b = 2

print(a, b)

print(a)
print(b)

answer = 7

print("정답은", answer, "입니다")

print(f"정답은 {answer} 입니다")

result = sum([1, 2, 3, 4, 5])
print(result)

result = min(7, 3, 5, 2)
print(result)

result = max(7, 3, 5, 2)
print(result)

result = eval("(3 + 5) * 7")
print(result)

result = sorted([9, 1, 8, 5, 4])
print(result)

result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)

result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1], reverse=True)
print(result)

from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print(result)

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))

print(result)


def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

import heapq


def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# bisect

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))

from collections import deque

data = deque([2, 4, 3])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

import math

print(math.factorial(5))

print(math.sqrt(7))

print(math.gcd(21, 14))

print(math.pi)
print(math.e)


def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]

    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(rotate_a_matrix_by_90_degree(a))

b = rotate_a_matrix_by_90_degree(a)

for i in range(len(b)):
    print(b[i])


import time


start_time = time.time()

end_time = time.time()

print("time : ", end_time - start_time)

from random import randint
import time


array = []
for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()
print("선택 정렬 성능 측정 : ", end_time - start_time)

array = []

for _ in range(10000):
    array.append(randint(1, 100))

start_time = time.time()

array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 : ", end_time - start_time)

