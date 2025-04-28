# 정수
a = 10
b = 20
c = 0
d = -40
print(type(a), type(b), type(c), type(d))
# ex
print(int(9.33333))

# 실수
number1 = 3.12
number2 = -0.12
print(type(number1), type(number2))
# ex
print(float(3))

# 무한대(infinity)
x = float("inf")
y = float("-inf")

# 문자열
str1 = "abcd"
str2 = 'abcd'
str3 = '''오늘은 4월 28일'''
print(type(str3))
print(str3)

# 문자열 이어붙이기
str4 = "modu"
str5 = "labs"
print(str4 + str5)
str6 = str4 + str5
print(str6)

str7 = str1 * 10
test1 = "30"
print(str7)
# print(str1 * test1) (x)
print(str7 + "입니다")

# ex)개인정보 출력해보기
## 1. 성, 이름 변수를 따로 만들어서 +로 합친 후 출력
## 2. 주민등록번호도 1번과 같이
## 3. 이메일 {아이디} {@} {네이버, 구글}
# 1번
fname = "Kim"
lname = "ajin"
print(fname + lname)
name = fname + lname
print(name)
# 2번
fnum = "990314"
lnum = "2987401"
print(fnum + "-" + lnum)
# 3번
id = "kaj123"
temp = "@"
adr = "naver.com"
# f-string 활용해서 출력
print(f"이메일 {id}{temp}{adr}")

# 문자열 인덱싱
## 마지막 문자는 인덱스번호가 -1이다 그 앞 문자는 -2
## 0부터 시작
s = "life is good"
print(s[0]) # l 출력
print(s[3]) # e 출력
print(s[-1]) # d 출력
## print(s[300]) 인덱스 범위를 벗어난 숫자이기 때문에 error 뜸
## 주민등록번호가 13자리
## print(s[13]) 에러 뜸
# 슬라이싱
print(s[0:3])   # lif 출력
## s[start:stop:step] stop은 출력하고싶은 문자의 다음문자로 적는다
## step은 점프기능 (생략가능)
print(s[0:4:2]) # lf 출력

#다양한 슬라이싱 방법
s = 'weniv CEO licat'
print(1, s[0:5]) # weniv 출력
print(2, s[6:]) # CEO licat 출력
print(3, s[:]) # weniv CEO licat 출력
print(4, s[::-1]) # tacil OEC vinew 출력
print(5, s[::2]) # wnvCOlct 출력

# ex)테스트
## ip address = 172.100.200.100
## 1. ip address문자열을 슬라이싱 기법 활용해 변수에 담아 출력
## 2. a,b,c,d라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다
## 3. f-string을 활용해 172100200100이 나오게 하기
adr = 'ip address = 172.100.200.100'
print(1, adr[:10])
a, b, c, d = adr[13:16], adr[17:20], adr[21:24], adr[25:28]
print(2, a,b,c,d)
print(3, f"{a}{b}{c}{d}")