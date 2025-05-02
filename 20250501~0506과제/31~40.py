# 31번 사칙연산 계산기
## 두 수와 연산자(+, -, *, /)를 입력받아 계산 결과를 출력하는 프로그램을 작성하세요.
a, b, c = int(input()), int(input()), input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)

# 32번 세금 계산기
## 금액과 세율(%)을 입력받아 세금과 세후 금액을 계산하는 프로그램을 작성하세요.
a, b = int(input()), int(input())
c = a * (b / 100)
d = a - c
print(f"세금 : {c:.1f}\n세후 금액 : {d:.1f}")

# 33번 논리 연산 테이블
## 두 불리언 값(True 또는 False)을 입력받아 AND, OR, NOT 연산 결과를 출력하는 프로그램을 작성하세요.
## a 가 True일 땐 출력 값이 True 아니면 False
a, b = input(), input()
a = a == "True"
b = b == "True"
print(f"{a} AND {b} : ", a and b)
print(f"{a} OR {b} : ", a or b)
print(f"NOT {a} : ", not a)
print(f"NOT {b} : ", not b)

# 34번 할인 계산기
## 원래 가격과 할인율(%)을 입력받아 할인 금액과 최종 가격을 계산하는 프로그램을 작성하세요.
a, b = int(input()), int(input())
c = a * (b / 100)
d = a - c
print(f"할인 금액 : {c:.1f}원\n최종가격 : {d:.1f}원")

# 35번 큰 수 판별
## 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 프로그램을 작성하세요.
a, b, c = int(input()), int(input()), int(input())
d = max(a, b, c)
print(f"가장 큰 수 : {d}")

# 36번 윤년 판별
## 연도를 입력받아 윤년인지 아닌지 판별하는 프로그램을 작성하세요.
## (윤년: 4로 나누어 떨어지고 100으로 나누어 떨어지지 않거나, 400으로 나누어 떨어지는 해)
a = input()
a = int(a)
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print(f"{a}년은 윤년입니다.")
else:
    print(f"{a}년은 윤년이 아닙니다.")

# 37번 문자열 포함 여부
## 두 문자열을 입력받아 첫 번째 문자열에 두 번째 문자열이 포함되어 있는지 확인하는 프로그램을 작성하세요.
a, b = input(), input()
if b in a:
    print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있습니다.")
else:
    print(f"\"{a}\"에 \"{b}\"이(가) 포함되어 있지 않습니다.")

# 38번 조건부 출력
## 점수를 입력받아 90점 이상이면 "A", 80점 이상이면 "B", 70점 이상이면 "C", 60점 이상이면 "D", 그 미만이면 "F" 등급을 출력하는 프로그램을 작성하세요.
a = int(input())
if a >= 90:
    print("학점 : A")
elif a >= 80:
    print("학점 : B")
elif a >= 70:
    print("학점 : C")
elif a >= 60:
    print("학점 : D")
else:
    print("학점 : F")

# 39번 자릿수 합계
## 양의 정수를 입력받아 각 자릿수의 합을 계산하는 프로그램을 작성하세요.
a = input()
b = sum(int(c) for c in a)
print(f"자릿 수 합계 : {b}")

# 40번 복합 조건
## 나이와 회원 여부(Y/N)를 입력받아 입장료를 출력하는 프로그램을 작성하세요.
a, b = int(input()), input()
if a >= 19 and (b == "N" or b == "n"):
    print("입장료 : 10000원")
elif a >= 19 and (b == "Y" or b == "y"):
    print("입장료 : 8000원")
elif a < 19:
    print("입장료 : 5000원")