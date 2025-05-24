# 함수의 기본 구조
def function_name(x, y):# x, y -> 파라미터 : 선언
    z = x + y
    return z
print(f"function_name(10, 9) = {function_name(10, 9)}")# 10, 9 -> 아규먼트 : 실행


# zip() : 여러 개의 순회할 수 있는 객체의 요소를 묶어서 반환
print(list(zip('abc', '1234567', [10, 20, 30])))
# [('a', '1', 10), ('b', '2', 20), ('c', '3', 30)] 출력
x = [1, 2, 3]
y = [1, 4, 9]
print(list(zip(x, y))) # [(1, 1), (2, 4), (3, 9)] 출력
x = [2, 4, 8, 16, 32, 64, 128]
print(list(zip(x, x[1:], x[2:])))
# [(2, 4, 8), (4, 8, 16), (8, 16, 32), (16, 32, 64), (32, 64, 128)] 출력


# format(값, '서식 지정자(format_spec)') : 특정 값을 지정된 형식으로 변환, 문자열로 반환
print(format(10000, ',')) # 10,000 출력
print(format(123.4567, '.2f')) # 123.46 출력


# len() : 길이를 계산
print(len('hello world')) # 11 출력


# max() : 최댓값 반환
## 수학점수가 가장 높은 사람을 반환
students = [
    {'이름': '가', '국어': 90, '영어':72, '수학': 95},
    {'이름': '나', '국어': 80, '영어':90, '수학': 91},
    {'이름': '다', '국어': 95, '영어':73, '수학': 92}
]
print(max(students, key=lambda student: student['수학']))
# {'이름': '가', '국어': 90, '영어': 72, '수학': 95} 출력
'''아렇게도 된다'''
def select(student):
    return student['수학']
students = [
    {'이름': '가', '국어': 90, '영어':72, '수학': 95},
    {'이름': '나', '국어': 80, '영어':90, '수학': 91},
    {'이름': '다', '국어': 95, '영어':73, '수학': 92}
]
print(max(students, key=select))


# min() : 최소값 반환
## 수학점수가 가장 낮은 사람을 반환
students = [
    {'이름': '가', '국어': 90, '영어':72, '수학': 95},
    {'이름': '나', '국어': 80, '영어':90, '수학': 91},
    {'이름': '다', '국어': 95, '영어':73, '수학': 92}
]
print(min(students, key=lambda student: student['수학']))
# {'이름': '나', '국어': 80, '영어': 90, '수학': 91} 출력
'''이렇게도 된다'''
def select(student):
    return student['수학']
students = [
    {'이름': '가', '국어': 90, '영어':72, '수학': 95},
    {'이름': '나', '국어': 80, '영어':90, '수학': 91},
    {'이름': '다', '국어': 95, '영어':73, '수학': 92}
]
print(min(students, key=select))


# sorted() : 오름차순 정렬 / reverse=True : 역순으로 정렬
print(sorted([1, 2, 100, 200, 3, 4, 10, 20], reverse=True))
# [200, 100, 20, 10, 4, 3, 2, 1] 출력


# 1. 함수를 이용하여 계산기 프로그램을 만들어주세요
def plus(num1, num2):
    return num1 + num2
def minus(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')