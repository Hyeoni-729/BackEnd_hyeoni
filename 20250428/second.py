# 입력 구현
## 파이썬에서는 숫자를 입력해도 input은 문자열(str)이다.
a = input("아무거나 입력해주세요 : ")
# 실행하면 input(입력)창에서 걸림 print는 출력x
print(a)
print("okay")

''' ex)입력을 몇 가지 변수에 담아서
f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력'''
name, age, adr = input(), input(), input()
print(f'이름은 {name}, 나이는 {age}, 사는곳은 {adr}')
print(name + age + adr)
print(name * 2 + age * 2 + adr * 2)

##형변환
print(type(a))
b = int(a) # 문자를 숫자로 변환
print(type(b))

# 문자열 메서드
s = 'weniv CEO licat'
print(s.lower()) # 문자 전체를 소문자로 변환
print(s.upper()) # 문자 전체를 대문자로 변환

# find(), index()
s = 'weniv CEO licat'
# print(s.find("good")) # -1(찾지 못 했다)출력
# print(s.index("good")) # 찾지 못 하면 error 코드 뜸
print(s.find("weniv")) # 인덱스번호 0부터 시작해서 0출력
print(s.find("licat")) # 인덱스번호 10부터 시작해서 10출력
print(s.index("weniv"))
print(s.index("licat"))

# count() 문자 갯수
s = 'weniv CEO licat'
print(s.count("i"))

# replace() 문자 교체
s2 = s.replace("CEO", "CTO")
print(s2)

# split() 문자열 나눔
s3 = "weniv corp"
s3.split() # "-" 전 후로 문자열이 나눠짐
# s4, s5 = s3.split("-") -> 나눈 문자열을 s4 s5로 각각 나눈다
print(s3)

''' ex)입력이 들어온다. 키 몸무게 성별 나이 이름
이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
이름을 f-string을 통해 세 번 반복해서 출력한다.'''
a = input()
height, weight, gen, age, name = a.split()
print(height, weight, gen, age, name)
print(f'{name * 3}')

# join() 리스트를 하나의 문자열로 합침
s1 = ["modu", "labs", "good"]
print("-".join(s1)) # modu-labs-good 출력

# 이스케이프 문자열
print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
print("Backslash: \\") # 백슬래시를 출력합니다.
'''
\n: 새로운 줄(줄바꿈)을 나타냅니다.
\t: 탭 문자를 나타냅니다.
\r: 커서를 현재 줄의 처음으로 이동합니다.
\": 큰따옴표를 나타냅니다.
\': 작은따옴표를 나타냅니다.
\\: 백슬래시를 나타냅니다.'''

# bool타입
a = 10 > 3
b = True # True와 False, None은 파이썬에서만 대문자를 쓴다
c = False
print(type(a)) # <class 'bool'> 출력
print(a) # True 출력
## 형변환
a = 1
b = 0
c = -1
d = 'okay'
e = ''
f = None # 아무것도 없다
print(bool(a)) # True
print(bool(b)) # False
print(bool(c)) # True
print(bool(d)) # True
print(bool(e)) # False
print(a==b) # False