# 11번 변수 교환
## 두 변수 a와 b의 값을 다중 할당을 사용하여 교환하는 프로그램을 작성하세요.
a, b = map(int, input().split())
c, d = b, a
print(f"교환 전 : a = {a}, b = {b}\n교환 후 : a = {c}, b = {d}")

# 12번 문자열 정보 출력
## 문자열을 입력받아 길이와 첫 글자, 마지막 글자를 출력하는 프로그램을 작성하세요.
a = input()
b = len(a)
print(f"문자열 길이 : {b}\n첫 글자 : {a[0]}\n마지막 글자 : {a[-1]}")  

'''
# 13번 이니셜 만들기 ☆(입력 시 영어로 해야하는지)
## 이름의 성과 이름을 공백으로 구분하여 입력받아 이니셜을 출력하세요. (예: "홍 길동" -> "H.G.")
fn = input().split()
fn1 = fn[0][0].upper()
fn2 = fn[1][0].upper()
print(f'이니셜 : {fn1}.{fn2}.')
'''

# 14번 소수점 자릿수
## 실수를 입력받아 소수점 2자리까지 표시하는 프로그램을 작성하세요.
a = float(input())
print(f"{a:.2f}")

# 15번 나이 구간 판별
## 나이를 입력받아 "미성년자"(19세 미만), "청년"(19-34세), "중장년"(35-64세), "노년"
age = int(input())
if age <= 19:
    print("미성년자")
elif 19 <= age <= 34:
    print("청년")
elif 35 <= age <= 64:
    print("중장년")
else:
    print("노년")

# 16번 문자열 분석
## 문자열을 입력받아 공백 수, 숫자 수, 문자 수를 출력하는 프로그램을 작성하세요.
## sum(a.count(str(e))for e in range(10))는 임의 변수 e에 문자열에서 0부터 9까지 총 등장 횟수를 더한 값
a = input()
b, c, d = a.count(" "), sum(a.count(str(e))for e in range(10)), sum(map(str.isalpha, a))
print(f'공백 수 : {b}\n숫자 수 : {c}\n문자 수 : {d}')

# 17번 참/거짓 변환
## 다양한 값을 불리언으로 변환한 결과를 출력하는 프로그램을 작성하세요.
a = int(input())
b = input()
if a == 0:
    print("False")
else:
    print("True")
if b == " ":
    print("False")
else:
    print("True")

# 18번 홀짝 판별
## 숫자를 입력받아 홀수인지 짝수인지 판별하는 프로그램을 작성하세요.
a = int(input())
if a % 2 == 0:
    print(f"{a}은(는) 짝수입니다.")
elif a % 2 == 1:
    print(f"{a}은(는) 홀수입니다.")

# 19번 문자열 분할
## 문장을 입력받아 쉼표(,)로 구분된 단어들로 분할하여 출력하는 프로그램을 작성하세요.
a = list(input().split())
print(",".join(a))

# 20번 온도 단위 변환기
## 온도와 단위(C/F)를 입력받아 다른 단위로 변환하는 프로그램을 작성하세요.
## C는 섭씨, F는 화씨를 의미합니다. (화씨 = 섭씨 * 9/5 + 32, 섭씨 = (화씨 - 32) * 5/9)
a = float(input())
b = input()
if b == "C" or b == "c":
    C = a
    F = (C * 9 / 5) + 32
    print(f"{C}°C는 {F:.1f}°F입니다.")
elif b == "F" or b == "f":
    F = a
    C = (F - 32) * 5 / 9
    print(f"{F:.1f}°F는 {C:.1f}°C입니다.")