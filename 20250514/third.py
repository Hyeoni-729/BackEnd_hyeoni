# # lambda
# - 이름이 없는 함수
# - 재사용 목적이 아니라 함수 기능 자체에 목적이 있다
# - 자주 사용되는 곳 : map, filter, sorted
def f(x):
    return x ** 2
list(map(f, [1, 2, 3, 4]))

# =======================================

list(map(lambda x: x ** 2, [1, 2, 3, 4]))
# lambda는 f값을 x와 x ** 2로 채워줌

# =======================================

# 문제 1 : [2, 5, 3, 7, 5, 3, 4, 1, 2, 3]에서 4 이상인 값을 모두 출력하세요. lambda를 통해 구현하세요.
list(filter(lambda x: x >= 4, [2, 5, 3, 7, 5, 3, 4, 1, 2, 3]))

# =======================================

# 상속
# 국내 학생

class Student:
    def __init__(self, name, score, phone, email):
        self.name = name
        self.score = score
        self.phone = phone
        self.email = email

    def __repr__(self):
        return self.name

# 외국학생이 들어왔습니다!? 1 / 10000 명이 들어왔어요.
# 이 한 명을 위해 이 class를 바꾸는 것이 바람직할까요?
# 그래서 이렇게 하고 싶은겁니다. Student에 있는 것을 그대로 사용하고
# 국적만 추가해주는 다른 class를 만드는 것입니다.

class ForeignStudent(Student):
    def __init__(self, name, score, phone, email, country):
        super().__init__(name, score, phone, email)
        self.country = country

# 그럼 이제 학생들 관리할 때 아래와 같이 관리할 수 있을 겁니다.

data = [
    Student("김민준", 85, "010-1234-5678", "minjun@example.kr"),
    Student("이서연", 92, "010-2345-6789", "seoyeon@example.kr"),
    Student("박지훈", 78, "010-3456-7890", "jihoon@example.kr"),
    Student("최수아", 88, "010-4567-8901", "sua@example.kr"),
    Student("정도현", 95, "010-5678-9012", "dohyun@example.kr"),
    Student("강하은", 82, "010-6789-0123", "haeun@example.kr"),
    Student("윤지우", 90, "010-7890-1234", "jiwoo@example.kr"),
    Student("임서진", 79, "010-8901-2345", "seojin@example.kr"),
    ForeignStudent("Emma Wilson", 87, "010-9012-3456", "emma@example.com", "USA"),
    Student("한유진", 93, "010-0123-4567", "yujin@example.kr")
]

data

# for i in data:
#     print(i.score)

# =======================================

class A:
    def move(self):
        print('움직여요!')

class B(A):
    pass

class C(B):
    pass

a = A()
b = B()
c = C()

a.move()
b.move()
c.move()

# =======================================

# 메서드 오버라이딩 ☆☆☆☆☆☆☆☆
class A:
    def move(self):
        print("출발")

class B(A):
    def move(self):
        print("덮어씀")

b = B()
b.move()

# =======================================

class MyClass:
    def __init__(self, c, d, e):
        self.__c = c
        self.d = d
        self._ = e

c = MyClass(30, 40, 50)
c._
c.__c # error