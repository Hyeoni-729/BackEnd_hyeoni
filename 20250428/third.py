# 산술연산자
result = 5 + 3
print(result) # 결과: 8
result = 3 + 2.5
print(result) # 결과: 5.5

# 나눗셈
'''첫번째 나눗셈 연산자는 항상 실수(float) 형식으로 반환되며,
두번째 나눗셈 연산자는 항상 정수(int)형으로 반환됩니다.
//는 내림입니다.'''
print(11/2) # 5.5 출력
print(10/2) # 5.0 출력
print(type(10/2)) # <class 'float'> 출력
print(11//2) # 5 출력

# 나머지
print(11%2 == 0) # False 출력
print(10%2 == 0) # True 출력