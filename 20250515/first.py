# 클로저
# 클로저 기법 사용 시 변수를 숨길 수 있다.
# factory 함수 기법이라고도 함.
# 클로저는 함수가 끝난 뒤에 휘발되어야 하는 영역에 함수가 끝난 뒤에도 접근 할 수 있도록 하는 기술
# x가 휘발되지 않으려면 어딘가에서 x를 사용하고 있기만 하면 된다.

# -----------------
def f(x):
    def ff(y):
        return y ** x
    return ff
aa = f(3)
# -----------------

# 위의 코드는 아래 코드와 같은 코드.
def aa(y):
    return y ** 3

# =======================================

def aa(y):
    return y ** 3
aa(2) # 여기 이후로는 x에 접근 불가능

# =======================================

# 모듈과 패키지
## colab에서 임의폴더 만들었었음
import lubi # 내 폴더에서 먼저 lubi.py를 찾는다.

lubi.age
lubi.name
lubi.add(3, 4)

'''
# lubi.py 파일 내용
name = 'lubi'
age = 27

def add(x, y):
    return x + y

def mul(x, y):
    return x * y
'''

# print(type(lubi)) -> <class 'module'> 출력

# =======================================

import lubi as l # 내 폴더에서 먼저 lubi.py를 찾는다.

print(lubi.age)
print(lubi.name)
print(lubi.add(3, 4))

'''
# lubi.py 파일 내용
name = 'lubi'
age = 27

def add(x, y):
    return x + y

def mul(x, y):
    return x * y
'''

# print(type(lubi)) -> <class 'module'> 출력

# =======================================

# 이 코드의 문제 발생 조건
# 같은 age, name, add가 헷갈리게 할 수 있다
from lubi import age, name, add
from hyeon import age, name, add

print(age)
print(name)
print(add(3, 4))

# =======================================

# 위와 같은 문제가 있기 때문에
# 아래와 같이 import 또는 import + as를 권장한다.

import lubi as l # 내 폴더에서 먼저 lubi.py를 찾는다.
import hyeon as h # 내 폴더에서 먼저 hyeon.py를 찾는다.

print(lubi.age)
print(lubi.name)
print(lubi.add(3, 4))

print(h.age)
print(h.name)
print(h.add(3, 4))

'''
# lubi.py 파일 내용
name = 'lubi'
age = 27

def add(x, y):
    return x + y

def mul(x, y):
    return x * y
'''

# print(type(lubi)) -> <class 'module'> 출력

# =======================================

# import 연습문제
## 문제 1: 수학 모듈 만들기

# **문제 설명:**
# 수학 연산을 수행하는 `math_tools.py` 모듈을 만들고, 이를 불러와 사용하는 프로그램을 작성하세요.

# **요구사항:**
# 1. `math_tools.py` 파일을 만들고 다음 항목을 구현하세요.
#    - `pi` 변수: 3.14159 값을 저장
#    - `e` 변수: 2.71828 값을 저장
#    - `square(x)` 함수: 숫자의 제곱을 반환
#    - `cube(x)` 함수: 숫자의 세제곱을 반환
#    - `factorial(n)` 함수: n의 팩토리얼(n!)을 계산하여 반환

# 2. 각 import 방식에 따라 pi 값을 출력하고, 숫자 5의 제곱을 계산하여 출력하세요.

# **예상 결과:**
# ```
# 전체 import 방식으로 사용:
# Pi: 3.14159
# 5의 제곱: 25

# 별칭(as)으로 import하여 사용:
# Pi: 3.14159
# 5의 제곱: 25

# 특정 항목만 import하여 사용:
# Pi: 3.14159
# 5의 제곱: 25
# ```

# ## 문제 2: 학생 정보 관리 모듈 만들기

# **문제 설명:**
# 학생들의 정보를 관리하는 `student_info.py` 모듈을 만들고, 이를 활용하여 학생들의 정보를 출력하는 프로그램을 작성하세요.

# **요구사항:**
# 1. `student_info.py` 파일을 만들고 다음 항목을 구현하세요:
#    - `school_name` 변수: 학교 이름 (예: "파이썬 고등학교")
#    - `students` 리스트: 학생들의 이름을 담은 리스트 (최소 3명)
#    - `get_student_info(name)` 함수: 학생 이름이 주어지면 "{이름}은/는 {학교이름}의 학생입니다."라는 문자열 반환
#    - `count_students()` 함수: 학생 수를 반환

# 2. 두 가지 import 방식을 모두 사용하여
#    - 학교 이름 출력
#    - 첫 번째 학생의 정보 출력 (두 가지 import 방식 모두 사용)
#    - 전체 학생 수 출력 (별칭을 사용한 import 방식으로만)

# **예상 결과:**
# ```
# [별칭 import 방식]
# 학교 이름: 파이썬 고등학교
# 첫 번째 학생 정보: 홍길동은/는 파이썬 고등학교의 학생입니다.
# 전체 학생 수: 3

# [특정 항목 import 방식]
# 학교 이름: 파이썬 고등학교
# 첫 번째 학생 정보: 홍길동은/는 파이썬 고등학교의 학생입니다.

# =======================================

# 문제 1번
## 전체 import 방식으로 사용
import math_tools
math_tools.pi
math_tools.square(5)

## 별칭(as)으로 import하여 사용
import math_tools as mt
mt.pi
mt.square(5)

## 특정 항목만 import하여 사용
from math_tools import pi, square
pi
square(5)

# =======================================

# 문제 2번
## 학교이름 출력
### 첫 번째 학생의 정보 출력(두 가지 import 방식 모두 사용)
import student_info
student_info.school_name
student_info.get_student_info(student_info.students[0])

### 전체 학생 수 출력(별칭<as>을 사용한 import 방식으로만)
import student_info as si
si.school_name
si.count_students()
si.get_student_info(si.students[0])

# =======================================

# 모듈을 읽는 순서
# 1.   해당 메모리에 해당 모듈이 있는지 확인
# 2.   해당 파일 폴더에 해당 .py파일이나 폴더가 있는지 확인
# 3.   파이썬이 설치된 곳으로 이동해서 모듈 찾음
# 4.   못 찾을 경우 에러를 반환

from a.b.c import lubi # a폴더 아래 b폴더 아래 c폴더 아래 lubi 파일
lubi.age

from a.b.c.lubi import age # 특정 항목(age)를 import로 써서 출력
age

# =======================================

# os 모듈
import os

os.mkdir('licat') # licat이란 폴더 생성, 삭제는 os.rmdir()
print(os.path.join('hello', 'world')) # 경로를 합쳐줌
print(os.listdir()) # 현재 디렉토리의 파일 목록 반환

# =======================================

# pathlib 모듈
## os 모듈보다 더 간단한 모듈
from pathlib import Path as p

p.cwd() # 현재경로 확인
pwd = p.cwd()
pwd / 'hello' / 'world' # /로 경로 결합

print(pwd / 'hello' / 'world100' / 'hello200') # Django에서도 많이 보는 코드

# =======================================

# pwd 인스턴스 입장에서는 /는 __truediv__가 호출, 여기서 나누기 하지않고 경로 결합해주는 코드가 작성됨
# 1. '/' (일반 나눗셈): `__truediv__` 매직 메서드가 처리합니다.
#    - 결과는 실수(float)를 반환합니다.
#    - 예: `5 / 2 = 2.5`

# 2. '//' (정수 나눗셈): `__floordiv__` 매직 메서드가 처리합니다.
#    - 결과는 몫만 반환하고, 소수점 이하를 버립니다.
#    - 예: `5 // 2 = 2`

# =======================================

# ☆☆☆☆☆
# datetime 모듈
from datetime import datetime

datetime.today()

# =======================================

today = datetime.today()
today.year
today.month
today.day
today.hour

# =======================================

import datetime
today = datetime.date.today()
days = datetime.timedelta(days = 100)
today + days # 100일 후 시간

# =======================================

import datetime

date = '2024-12-10'
date = datetime.datetime.strptime(date, '%Y-%m-%d')
print(date)

# https://docs.python.org/ko/3/library/datetime.html#strftime-and-strptime-format-codes

# =======================================

# json 모듈
## Python 데이터 구조를 JSON 문자열로 직렬화하거나
## JSON 문자열을 Python 데이터 구조로 역직렬화하는 기능을 제공합니다.
## 일반적으로 클래스로 구현하여 만든 인스턴스는 직렬화되지 않습니다.

import json

d = {
    'one': 1,
    'two': 2,
    'three': 3
}

# s = json.dumps(d)
# print(type(s)) # str
# d = json.loads(s)
# print(type(d)) # dict

# str(d)
json.dumps(d) # str(d) 보다 좀 더 안전하고, 견고하게 바꿔줌

# =======================================

import json

d = {
    'one': 1,
    'two': 2,
    'three': True
}

str(d) # {'one': 1, 'two': 2, 'three': True} 출력
# json.dumps(d) -> str(d) 보다 좀 더 안전하고, 견고하게 바꿔줌 {'one': 1, 'two': 2, 'three': true} 출력

# =======================================

# # 예외처리
# - 에러를 만나면 에러를 외워야 함
# - 모든 코드에 try와 except를 작성하는 것은 X
# 예외처리
# ☆☆☆☆☆☆

try:
    pass
except:
    pass

# =======================================

try:
    for i in range(10):
        print(i)
except:
    print('에러발생')

print('종료')

# =======================================

try:
    for i in range(10):
        print(i)
        1/0
except:
    print('에러발생했으니 다시 시도')

print('종료')

# =======================================

try:
    s = 1/0
    print(s)
except ZeroDivisionError:
    print('0으로 나누어졌습니다!')

# =======================================

# '11111122222312312312312344433322111'
# => 1은 !로
# => 2는 @로
# => 3은 #로
# => 4는 $로

s = '11111122222312312312312344433322111'
s.replace('1', '!').replace('2', '@').replace('3', '#').replace('4', '$')

# =======================================

# 이렇게 반환값이 중간에 list로 바뀌면 사용x
s = '11111 2222 33333'
s.replace('1', '!').split(' ') # 이 다음에 replace를 연달아 사용 못 함. 이까지가 list이기 때문에

# =======================================

# 함수를 아규먼트로 넣는 것
def a(x):
    return x ** 2

def b(x):
    return x ** 3

# 함수를 리턴 값으로 넣는 것
def cal(f, ff, x):
    return f(x) + ff(x)

cal(a, b, 2)

# =======================================

# 함수를 아규먼트로 넣는 것
def a(x):
    return x ** 2

def b(x):
    return x ** 3

# 함수를 리턴 값으로 넣는 것
def cal(f):
    return b

cal(a)(2) # cal(a) : b -> b(2) -> 8출력

# =======================================

# 재귀함수
def hello():
    print(1)
    return hello() # 내가 나를 호출하는 무한반복 함수

# =======================================

result = 1
for i in range(1, 6):
    result *= i

result # 5!(5*4*3*2*1)

# =======================================

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(5)

# 함수 아규먼트         return 값               출력 값
# factorial(5)          5 * factorial(4)    =   120
# factorial(4)          4 * factorial(3)    =   24
# factorial(3)          3 * factorial(2)    =   6
# factorial(2)          2 * factorial(1)    =   2
# factorial(1)          1

# =======================================

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

inner = outer_function(100)
inner(200) # inner

# 위 코드는 아래 코드와 같습니다.
# def inner(y):
#     return 100 + y

# =======================================

def f(x):
    def ff(y):
        return y ** x
    return ff

a = f(2)
a(2)
a(3)
a(4)
b = f(3)
b(2)
b(3)
b(4)

# =======================================

def simple_decorator(function):
    def wrapper():
        print("전")
        function()
        print("후")
    return wrapper

@simple_decorator
def hello():
    print("Hello, World!")

hello() # 데코레이터가 없는 상태에서는 simple_decorator(hello)()와 같다
