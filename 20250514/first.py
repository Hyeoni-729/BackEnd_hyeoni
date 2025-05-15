# break, continue는 while과 for에서 모두 사용가능
# break는 반복문 중단, continue는 다음 반복문으로 넘어감
import random
result = random.randint(1, 100)

while True:
    user_input = int(input("숫자를 입력하세요(1 ~ 100) : "))
    if user_input > result:
        print("더 작은 숫자를 입력하세요")
    elif user_input < result:
        print("더 큰 숫자를 입력하세요")
    else:
        print("정답입니다")
        break # 반복문 탈출

# =======================================

# 클래스
# 클래스 ▶ 설계 도면
# 인스턴스 ▶ 생산품
# 클래스 내의 변수 ▶ 멤버 또는 애트리뷰트
# 클래스 내의 함수 ▶ 메서드
# 클래스 변수 ▶ 설계 도면에 포함되어야 하는 것
# 인스턴스 변수 ▶ 생산품에 포함되어야 하는 것

# 자동차!
# 데이터(멤버, 애트리뷰트) # 클래스 내 변수로 선언됩니다. 이것을 멤버 또는 애트리뷰트라고 합니다.
#   * 최대 속도
#   * 최대 탑승객
class Car:
    # 클래스 변수 위치
    max_speed = 300 # 멤버 or 애트리뷰트
    max_people = 5

    def start(self): # 메서드
        print('출발')

    def stop(self):
        print('정지')
car1 = Car() # Car() : 클래스 / car1 : 인스턴스
car2 = Car()

print(car1.max_speed)
car1.start()

# =======================================

class Car:
    # 클래스 변수 위치
    max_speed = 300
    max_people = 5
modelx = Car()

# =======================================

# self : 해당 인스턴스
class Car:
    # 클래스 변수 위치
    max_speed = 300
    max_people = 5

    def __init__(self, 구매자): # __init__ : 매직메서드 / self, 구매자 : 파라미터
        # 인스턴스 변수 위치
        # 'self.변수이름'의 형태
        self.차구매자 = 구매자
modela = Car('구매자1')
modelb = Car('구매자2')

print(modela.차구매자)
print(modelb.차구매자)

# =======================================

# self : 해당 인스턴스
class Car:
    # 클래스 변수 위치
    max_speed = 300
    max_people = 5

    def __init__(self, 구매자): # __init__ : 매직메서드 / self, 구매자 : 파라미터
        # 인스턴스 변수 위치
        # 'self.변수이름'의 형태
        self.차구매자 = 구매자
modela = Car('구매자1')
modelb = Car('구매자2')

# 인스턴스 변수를 이래 넣을수도 있다
modela.스마트키 = '키티 스마트키'
print(modela.스마트키)

# =======================================

# 기능(메서드) # 클래스 내 함수로 선언됩니다. 이것을 메서드라고 합니다.
#   * 출발
#   * 정지

# =======================================

# 항공사, 편명, 좌석번호, 이름, 나이, 짐무게(kg), 마일리지
data = [
    ['대한항공', 'KE607', '12A', '김민준', 42, 23, 5280],
    ['아시아나', 'OZ721', '8C', '이', 29, 18, 3450],
    ['제주항공', '7C101', '15F', '박지민', 35, 15, 720],
    ['진에어', 'LJ211', '4D', '최서우미래한별', 51, 27, 8900],
    ['에어부산', 'BX213', '21B', '정', 24, 12, 1250],
    ['티웨이', 'TW305', '19E', '강민석', 38, 20, 2760],
    ['에어서울', 'RS808', '3C', '윤지현', 47, 16, 4320],
    ['대한항공', 'KE123', '7F', '송', 33, 21, 6780],
    ['아시아나', 'OZ562', '11D', '장하은별님달빛', 26, 19, 1890],
    ['제주항공', '7C505', '17B', '황수진', 40, 14, 940]
]
class Passenger:
    def __init__(self, 항공사, 편명, 좌석번호, 이름, 나이, 짐무게, 마일리지):
        self.항공사 = 항공사
        self.편명 = 편명
        self.좌석번호 = 좌석번호
        self.이름 = 이름
        self.나이 = 나이
        self.짐무게 = 짐무게
        self.마일리지 = 마일리지

    def __str__(self):
        return f'{self.이름}, {self.나이}'

    def __add__(self, next):
        return self.마일리지 + next.마일리지
p1 = Passenger('대한항공', 'KE607', '12A', '김민준', 42, 23, 5280)
p2 = Passenger('아시아나', 'OZ721', '8C', '이', 29, 18, 3450)
p3 = Passenger('제주항공', '7C101', '15F', '박지민', 35, 15, 720)

print(p1) # 원하는 정보만 출력한 것입니다.
print(p1 + p2) # 마일리지 더한 것입니다.

# =======================================

class Car:
    # 클래스 변수 위치
    max_speed = 300
    max_people = 5

    def __init__(self, 구매자): # __init__ : 매직메서드 / self, 구매자 : 파라미터
        # 클래스가 인스턴스를 찍어낼 때 자동으로 실행
        # 인스턴스 변수 위치
        # 'self.변수이름'의 형태
        self.차구매자 = 구매자
modela = Car('구매자1') # Car.__init__(modela, '구매자1') 과 유사한 코드
modelb = Car('구매자2')

# modela + modelb -> '+'기호는 modela에 __add__를 실행 <오류 뜸>

# =======================================

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, next):
        return [self.x + next.x, self.y + next.y]

    def __mul__(self, next):
        return [self.x * next.x, self.y * next.y]

a = Dot(1, 1)
b = Dot(2, 2)

a + b

# =======================================

class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, next):
        return False

a = Dot(1, 1)
b = Dot(2, 2)

a == b # '=='기호는 a에 __eq__를 실행합니다!

# =======================================

l = [10, 20] # l은 list라는 클래스에 인스턴스입니다!
ll = [10, 20] # ll은 list라는 클래스에 인스턴스입니다!

l == ll # l인스턴스의 __eq__를 실행시킨 결과를 보여주세요!

a = 10 # a는 int라는 클래스에 인스턴스 입니다!
b = 20 # b는 int라는 클래스에 인스턴스 입니다!

a + b # a인스턴스의 __add__를 실행시킨 결과를 보여주세요!
a * b # a인스턴스의 __mul__를 실행시킨 결과를 보여주세요!

# =======================================

class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, next):
        # return False
        return self.x == next.x and self.y == next.y

a = Dot(1, 1)
b = Dot(1, 2)

a == b # '=='기호는 a에 __eq__를 실행합니다!

# =======================================

class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # return f'<{self.x}, {self.y}>'
        return 'hello world'

a = Dot(1, 1)
b = Dot(2, 2)

print(a) # print는 a의 __str__을 실행합니다.
print(b) # print는 a의 __str__을 실행합니다.

# print(a) -> <__main__.Dot object at 0x7f8486df35d0> 출력