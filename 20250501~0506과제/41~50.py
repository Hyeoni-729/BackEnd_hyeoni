# 41번 비밀번호 강도 검사
## 비밀번호를 입력받아 길이가 8자 이상이고 문자와 숫자가 모두 포함되어 있는지 확인하는 프로그램을 작성하세요.
## any(): 내부 조건이 하나라도 참이면 True를 반환합니다.
## isalpha(): 문자인지 확인 (A–Z, a–z).
## isdigit(): 숫자인지 확인 (0–9).
## len(a) >= 8: 8자 이상인지 확인.
a = input()
b = any(i.isalpha() for i in a)
c = any(i.isdigit() for i in a)
if b and c and len(a) >= 8:
    print("안전한 비밀번호입니다.")
else:
    print("안전하지 않은 비밀번호입니다.")

# 42번 단어 뒤집기
## 여러 단어로 이루어진 문장을 입력받아 각 단어를 뒤집어서 출력하는 프로그램을 작성하세요.
a = list(input().split())
print(' '.join(b[::-1] for b in a))

'''
# 43번 문자 카운터 ☆☆☆☆☆☆☆
## 문장을 입력받아 모음(a, e, i, o, u)과 자음의 개수를 출력하는 프로그램을 작성하세요.
a = input()
## 모음을 대소문자 모두 포함한 문자열로 정의합니다.
a1 = "aeiouAEIOU"
## 자음을 대소문자 모두 포함한 문자열로 정의합니다.
a2 = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" 
## sum(1 for char in a if char in a1) : 문장에서 모음에 해당하는 문자들을 세고, 자음에 대해서도 같은 방식
b = sum(1 for char in a if char in a1)
c = sum(1 for char in a if char in a2)
print(f"모음 개수 : {b}\n자음 개수 : {c}")
'''

# 44번 근삿값 계산
## 실수를 입력받아 가장 가까운 정수를 계산하는 프로그램을 작성하세요.
a = float(input())
b = round(a)
print(f"가장 가까운 정수 : {b}")

'''
# 45번 날짜 유효성 검사 ☆☆☆☆☆☆☆
## 연월일(YYYY-MM-DD 형식)을 입력받아 유효한 날짜인지 검사하는 프로그램을 작성하세요.
'''

# 46번 파일 확장자 추출
## 파일명을 입력받아 확장자를 추출하는 프로그램을 작성하세요. (예: "document.txt" -> "txt")
a = input()
if '.' in a:
    b = a.split('.')[-1] ## [-1]은 '.'기준 맨 끝 리스트 출력
    print(f"확장자 : {b}")
else:
    print("확장자가 잘못 입력되었습니다.")

'''
#47번 문자열 압축 ☆☆☆☆☆☆☆
## 연속된 문자를 문자와 개수로 압축하는 프로그램을 작성하세요. (예: "aabbbcccc" -> "a2b3c4")
'''

# 48번 팰린드롬 검사
## 입력된 문자열이 앞뒤로 읽어도 같은 팰린드롬인지 검사하는 프로그램을 작성하세요.
a = input()
if a == a[::-1]:
    print(f'{a}는 팰린드롬입니다.')
else:
    print(f'{a}는 팰린드롬이 아닙니다.')

'''
# 49번 간단한 암호화 ☆☆☆☆☆☆☆
## 문자열을 입력받아 각 문자를 3글자씩 뒤로 미루는 시저 암호로 암호화하는 프로그램을 작성하세요.
a = input() ## 문자열 입력 받기
b = ''.join( ## 암호화 (3글자 뒤로)
    chr((ord(c) - ord('A') + 3) % 26 + ord('A')) if c.isupper()
    else chr((ord(c) - ord('a') + 3) % 26 + ord('a')) if c.islower()
    else c
    for c in a
)
print(f"암호화 : {b}") ## 결과 출력
'''

# 50번 IP 주소 검증
## IP 주소를 입력받아 각 부분이 0-255 사이의 숫자인지 검증하는 프로그램을 작성하세요.
## a.split("."): .을 기준으로 IP 주소를 4부분으로 나눕니다.
## c.isdigit(): 각 부분이 숫자로만 이루어졌는지 확인.
## 0 <= int(c) <= 255: 숫자 범위가 올바른지 확인.
## all(...): 모든 조건이 참이어야 전체 결과가 참이 됩니다.
## len(b) == 4: IP 주소는 반드시 4개의 부분으로 되어 있어야 합니다.
a = input()
b = a.split(".")
if len(b) == 4 and all(c.isdigit() and 0 <= int(c) <= 255 for c in b):
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")