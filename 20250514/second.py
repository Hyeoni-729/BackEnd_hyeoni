# 클래스 연습문제
# 문제 1: 간단한 Book 클래스 만들기
### 책을 표현하는 Book 클래스를 만들어보세요. 책은 제목, 저자, 페이지 수를 가지며, 책 정보를 출력하는 기능이 있어야 합니다.

# - Book 클래스를 구현하세요
# - 요구사항:
# - 1. 제목(title), 저자(author), 페이지 수(pages)를 속성으로 가짐
# - 2. __str__ 메서드를 구현하여 책 정보를 "제목 (저자, 페이지수 쪽)" 형식으로 출력
# - 3. book1과 book2를 비교했을 때 페이지 수가 많은 책이 "더 큰" 책이 되도록 __gt__ 메서드 구현

#### 예시 실행 코드
# book1 = Book("파이썬 기초", "김코딩", 200)
# book2 = Book("자바 기초", "이자바", 300)

# print(book1)  # 출력 예상: 파이썬 기초 (김코딩, 200 쪽)
# print(book2 > book1)  # 출력 예상: True (300 > 200)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): # __str__ : print 문으로 객체를 출력할 때 사용됨
        return f'{self.title} ({self.author}, {self.pages} 쪽)'
    def __gt__(self, next): # __gt__ : > 연산을 오버라이드할 때 쓰임, next : 비교대상(페이지 수가 더 많은 책)
        return self.pages > next.pages
book1 = Book("파이썬 기초", "김코딩", 200)
book2 = Book("자바 기초", "이자바", 300)
print(book1)
print(book2 > book1)

# =======================================

# 문제 1 강사님 풀이
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} ({self.author}, {self.pages} 쪽)'

    def __gt__(self, next):
        return self.pages > next.pages
    
# =======================================

# 문제 2: 계산기 클래스 만들기
### 사칙연산을 수행할 수 있는 Calculator 클래스를 만들어보세요.

# - Calculator 클래스를 구현하세요
# - 요구사항:
# - 1. 덧셈, 뺄셈, 곱셈, 나눗셈 기능 구현
# - 2. 계산 기록을 저장하는 기능 추가
# - 3. 마지막 계산 결과를 기억하고 있어야 함

#### 예시 실행 코드
# calc = Calculator()
# print(calc.add(5, 3))  # 출력 예상: 8
# print(calc.subtract(10, 7))  # 출력 예상: 3
# print(calc.multiply(4, 2))  # 출력 예상: 8
# print(calc.divide(9, 3))  # 출력 예상: 3.0
# print(calc.get_history())  # 출력 예상: ['5 + 3 = 8', '10 - 7 = 3', '4 * 2 = 8', '9 / 3 = 3.0']
# print(calc.get_last_result())  # 출력 예상: 3.0

class Calculator:
    def __init__(self): # history와 last_result 초기 설정
        self.history = []
        self.last_result = None
    def add(self, a, b):
        result = a + b
        self._save_history(a, b, '+', result) # _save_history() : 중복제거와 책임분리에 도움
        return result
    def subtract(self, a, b):
        result = a - b
        self._save_history(a, b, '-', result)
        return result
    def multiply(self, a, b):
        result = a * b
        self._save_history(a, b, '*', result)
        return result
    def divide(self, a, b):
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다") # 예외처리
        result = a / b
        self._save_history(a, b, '/', result)
        return result

    def _save_history(self, a, b, operator, result):
        record = f"{a} {operator} {b} = {result}"
        self.history.append(record)
        self.last_result = result

    def get_history(self):
        return self.history

    def get_last_result(self):
        return self.last_result

calc = Calculator()
print(calc.add(5, 3))            # 8
print(calc.subtract(10, 7))      # 3
print(calc.multiply(4, 2))       # 8
print(calc.divide(9, 3))         # 3.0
print(calc.get_history())        # ['5 + 3 = 8', '10 - 7 = 3', '4 * 2 = 8', '9 / 3 = 3.0']
print(calc.get_last_result())    # 3.0

# =======================================

# 문제 2 강사님 풀이
class Calculator:
    def __init__(self):
        self.history = []
    def add(self, a, b):
        self.history.append(f"{a} + {b} = {a + b}")
        return a + b
    def subtract(self, a, b):
        self.history.append(f"{a} - {b} = {a - b}")
        return a - b
    def multiply(self, a, b):
        self.history.append(f"{a} * {b} = {a * b}")
        return a * b
    def divide(self, a, b):
        self.history.append(f"{a} / {b} = {a / b}")
        return a / b
    def get_history(self):
        return self.history
    def get_last_result(self):
        return self.history[-1]
    
# =======================================

# 문제 3: 간단한 학생 성적 관리 클래스 만들기
### 학생들의 성적을 관리하는 GradeBook 클래스를 만들어보세요.

# - GradeBook 클래스를 구현하세요
# - 요구사항:
# - 1. 학생 이름과 점수를 추가하는 기능
# - 2. 전체 학생 목록과 점수를 출력하는 기능
# - 3. 최고 점수와 해당 학생 이름을 반환하는 기능
# - 4. 평균 점수를 계산하는 기능

#### 예시 실행 코드
# gradebook = GradeBook()
# gradebook.add_student("김철수", 85)
# gradebook.add_student("이영희", 92)
# gradebook.add_student("박민수", 78)
# gradebook.add_student("정지원", 95)

# gradebook.print_grades()  # 모든 학생의 이름과 점수 출력
# print(f"최고 점수: {gradebook.get_highest_grade()}")  # 출력 예상: 최고 점수: ('정지원', 95)
# print(f"평균 점수: {gradebook.get_average()}")  # 출력 예상: 평균 점수: 87.5

class GradeBook:
    def __init__(self):
        self.students = {}

    def add_student(self, name, score):
        self.students[name] = score # self.students : 딕셔너리, name : key, score : value로 저장
        # 이미 존재하는 학생 이름이 들어오면 기존 점수를 덮어씀(수정 가능)

    def print_grades(self):
        for name, score in self.students.items():
            print(f'{name} : {score}점')

    def get_highest_grade(self):
        if not self.students:
            return None
        highest_student = max(self.students.items(), key=lambda x: x[1])
        # highest_student = max(self.students.items(), key=lambda x: x[1])
        # self.students.items() -> (이름, 점수) 튜플의 iterable 반환
        # key=lambda x: x[1] → 점수(x[1]) 기준으로 최대값 찾기
        return highest_student

    def get_average(self):
        if not self.students:
            return None
        total = sum(self.students.values())
        count = len(self.students)
        return total / count
gradebook = GradeBook()
gradebook.add_student("김철수", 85)
gradebook.add_student("이영희", 92)
gradebook.add_student("박민수", 78)
gradebook.add_student("정지원", 95)

gradebook.print_grades()
print(f"최고 점수: {gradebook.get_highest_grade()}")  # ('정지원', 95)
print(f"평균 점수: {gradebook.get_average()}")        # 87.5

# =======================================

# 문제 3 강사님 풀이
class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, name, score):
        self.students.append((name, score))

    def print_grades(self):
        return self.students

    def get_highest_grade(self):
        def f(x):
            return x[1]
        return sorted(self.students, key=f, reverse=True)[0]

    def get_average(self):
        def f(x):
            return x[1]
        return sum(map(f, self.students)) / len(self.students)
    
# =======================================    

## 나아가기
## 실무라면 어떻게 하는 것이 좋았을까요?
## class로 변환 할 수 있는 것은 모두 클래스로 변경

class Student:
    def __init__(self, name, score, phone, email):
        self.name = name
        self.score = score
        self.phone = phone
        self.email = email

    def __str__(self): # print를 하면 출력해주는 문자열
        return f'{self.name}'

    def __repr__(self): # 이 객체를 대표하는 문자열, print를 안하고 출력하면 이 문자열을 출력합니다.
        return f'{self.name}'

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, name, score, phone='000-0000-0000', email=''):
        self.students.append(Student(name, score, phone, email))

    def print_grades(self):
        return self.students

# 예시 실행 코드
gradebook = GradeBook()
gradebook.add_student("김철수", 85, '010-0000-0000')
gradebook.add_student("이영희", 92)
gradebook.add_student("박민수", 78)
gradebook.add_student("정지원", 95)

gradebook.print_grades()

data = gradebook.print_grades()
data[0].score
data[0].phone