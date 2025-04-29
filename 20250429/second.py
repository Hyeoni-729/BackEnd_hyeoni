# and 연산
## 둘 다 True여야 True 출력
# or 연산
## 둘 중에 하나라도 True면 True 출력
# a && b
a = True
b = True
c = a and b

d = 10 > 5 and 10 < 5
print(d) # False 출력

e = 10 >= 5 or False # 이미 앞이 True이기 때문에 무조건 True 출력
print(e)

f = False and True and True # 0 1 1
print(f) # False 출력

g = (False or True) and True # (1) and 1
print(g) # True 출력

# not 연산
h = not((False or True) and True) # not((1)and1)
print(h) # 1의 not -> 0 False 출력

i = 10
j = 20
k = i != j # i와 j가 다르니? 묻는 부등호 # True 출력
l = not i != j # i와 j가 다르니?의 반대 # False 출력
# ex) 항은 3개 이상 and, or는 마음대로 연결하여 결과 출력
a = int(input())
b = int(input())
c = int(input())

d = a != b
e = not a != b
f = ((a + b) < 10) or ((a + b) >= 10)
print(d)
print(e)
print(f)

st = "monulabs is good"
sta = "good" in st # st 안에 "good" 문자가 있니?
#sta = "good" not in st # st 안에 "good" 문자가 없니?
print(sta)

# 파이썬 codeup 문제 6045번
## 정수 3개 입력받아 합과 평균 출력하기, 소수점기준 3자리까지 출력
a, b, c = input().split() # 공백으로 구분된 한 줄로 값들을 입력받기
a, b, c = int(a), int(b), int(c)
sum = a + b + c
avg = sum / 3
print(sum, f'{avg:.3f}')