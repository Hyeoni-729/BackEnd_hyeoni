# function
## 파라미터와 아규먼트
## xysum(x, y) -> 함수를 정의 / x, y는 파라미터
## print(xysum(10, 20)) -> 함수를 호출 / 10, 20은 아규먼트
def xysum(x, y):
    return x + y
print(xysum(10, 20))  # 30출력

"""
ex1) 2x + 15 방정식, x는 10이라고 주어졌을 때, y값이 얼마인지 구하는 함수를 만드세요
"""
def solution(x):
    y = 2 * x + 15
    return y
print(solution(10))  # 35출력

"""
ex2) [10, 20, 30] + [1, 2, 3]이라고 했을 때 두 리스트를 요소별로 더하는 함수를 만드세요.
"""
def solution(a, b):
    # enumerate(리스트a, start<기본값이 0>) = range(len(a))
    for i, j in enumerate(a):
        a[i] = j + b[i]
    return a
print(solution([10, 20, 30], [1, 2, 3]))  # [11, 22, 33]출력

"""
ex3) 리스트의 모든 요소에 특정 숫자를 곱하는 함수를 만드세요
"""
def solution(matrix, multiplier):
    result = []
    for i in matrix:
        result.append(i * multiplier)
    return result
print(solution([1, 2, 3, 4], 2)) # [2, 4, 6, 8]출력

"""
ex4) 정수가 담긴 리스트 num_list가 주어집니다.
num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을
return하도록 solution 함수를 완성해주세요.
"""
def solution(num_list):
    a, b = '', ''
    for i in num_list:
        if i % 2 == 0:
            a += str(i)
        else:
            b += str(i)
    answer = int(a) + int(b)
    return answer
print(solution([3, 4, 5, 2, 1])) # 393출력

## 지역변수, 전역변수
x = 10 # 전역변수
def hello():
    x = 100 # 지역변수 : 밖에 있는 변수 수정 불가능
hello()
print(x)