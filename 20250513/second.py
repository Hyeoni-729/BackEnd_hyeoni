# type, dir, id
## dir은 해당 자료형에 있는 속성들을 파악하기 좋다.
## id는 해당 자료형이 무엇을 가리키고 있는지 확인하기 좋다.

# python built-in functions
## abs(-10) # 절대값으로 바꿔줌
## all([True, True, False]) # 안에 값이 다 True여야 True
## any([True, True, False]) # 안에 값이 하나라도 True라면 True
## bin(10) # 2진수로 바꿔준다, 알고리즘 문제에서 가끔 출제
## enumerate
## len
## format
## input
## range
## sorted ☆☆☆☆☆
"""
s = [10, 20, 5, 4, 3, 8, 19, 3, 2]
sorted(s) # 오름차순
sorted(s, reverse=True) # 내림차순"""
# sorted ex)
# 학년, 반, 번, 이름, 국어, 영어, 수학
data = [
    [1, 1, 5, '홍길동', 78, 54, 39],          # 3
    [1, 1, 2, '김철수', 92, 88, 75],          # 3
    [1, 2, 7, '이', 87, 91, 82],              # 1
    [1, 2, 3, '박민수', 65, 72, 84],          # 3
    [1, 1, 8, '정수진', 91, 85, 93],          # 3
    [1, 3, 1, '강', 76, 79, 88],              # 1
    [1, 2, 4, '윤서연미래별하', 89, 94, 90],  # 7
    [1, 3, 6, '장현우', 82, 67, 71],          # 3
    [1, 1, 10, '조', 95, 89, 97],             # 1
    [1, 3, 9, '최준호빛나라', 73, 80, 76]     # 6
    ]

"""1번 : 이름의 글자 수 대로 정렬해라"""
def f(x):
    return len(x[3])
print(sorted(data, key=f))
# sorted(data, key=f)
## sorted의 파라미터가 key로 정해져있음
## key=함수(일반 def되는 함수 & lambda함수 모두 함수의 형태면 가능)
## 함수의 return 값에 따라 정렬을 해준다

"""2번 : 평균대로 정렬해라"""
def f(x):
    return sum(x[4:])
print(sorted(data, key=f, reverse=True))
# print(sorted(data, key=f, reverse=True))
## 일반적으로 정수 정렬은 reverse=True가 붙는다

"""3번 : 국어, 수학 점수가 가장 점수차가 큰 순서대로 정렬해라"""
def f(x):
    return abs(x[4] - x[6])
print(sorted(data, key=f, reverse=True))

"""
4번 : 1차원의 점들이 주어졌을 때,
그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)
예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.
"""
# data = [[1, 3], [3, 4], [4, 8], [8, 13], [13, 17], [17, 20]]
# def f(x):
#     return x[1] - x[0]
# print(sorted(data, key=f))
s = [1, 3, 4, 8, 13, 17, 20]
def f(x):
    return x[1] - x[0]
print(sorted(zip(s, s[1:]), key=f))

# sorted에서 자주 나오는 유형2번째
## 정렬 기준이 나한테 없는 경우
data1 = [
    'Moby Dick',              # 1851
    'To Kill a Mockingbird',  # 1960
    '1984'                    # 1949
    ]
data2 = {'Moby Dick': 1851, 'To Kill a Mockingbird': 1960, '1984': 1949}
def f(x):
    return data2[x]
print(sorted(data1, key=f))

# 우편번호 정렬
## 우편번호 오름차순 순서대로 주소를 정렬하는 코드
data = [['A동', 'B동', 'C동'], {'A동':63007, 'B동':63010, 'C동':63002}]
def f(x):
    return data[1][x]
print(sorted(data[0], key=f))

# reverse
## 이 두개는 성능이 떨어짐
list(reversed([10, 20, 30]))
list(range(10))