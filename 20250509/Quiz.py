# 주간 학습 점검
# 1번
## 다음 코드 실행 결과는?
"""답 : (2, 3, 4)"""
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:4])

# 2번
## 다음 코드를 실행한 후 리스트 numbers의 내용은 무엇인가요?
"""답 : (1, 3, 4, 5, 6)"""
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(2)
print(numbers)

# 3번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : 10"""
total = 0
for i in range(1, 5):
    total += i
print(total)

# 4번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : C"""
score = 75
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
else:
    result = "D"
print(result)

# 5번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : Progra"""
text = "Python Programming"
print(text[7:13])

# 6번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : 21"""
student = {"name": "Kim", "age": 20, "grade": "A"}
student["age"] = 21
print(student["age"])

# 7번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : 9"""
result = 0
for i in range(3):
    for j in range(2):
        result += i + j
print(result)

# 8번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : C"""
a = 5
b = 10
c = 15
if a > b:
    print("A")
elif b > c:
    print("B")
elif a + b == c:
    print("C")
else:
    print("D")

# 9번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : [3, 4, 5]"""
numbers = [2, 4, 6, 8, 10]
result = []
for num in numbers:
    if num > 5:
        result.append(num // 2)
print(result)

# 10번
## 다음 코드의 출력 결과는 무엇인가요?
"""답 : 12"""
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
result = 0
for key in data:
    for num in data[key]:
        if num % 2 == 0:
            result += num
print(result)

# 11번
"""
다음 코드의 빈칸을 채워 리스트 numbers에서 짝수만 골라내 새로운 리스트 even_numbers에 저장하는 코드를 완성하세요.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if ____________:
        ____________
       
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# 12번
"""
온도에 따라 상태를 출력하는 프로그램을 작성하세요.
온도가 0도 미만이면 "얼음" 온도가 0도 이상 100도 미만이면 "물" 온도가 100도 이상이면 "수증기" 를 출력합니다.
사용자로부터 온도를 입력받고 위 조건에 맞게 상태를 출력하는 코드를 작성하세요.
"""
user_temp = int(input())
if user_temp < 0:
    print("얼음")
elif 0 <= user_temp < 100:
    print("물")
elif 100 <= user_temp:
    print("수증기")

# 13번
"""
다음의 학생 점수 딕셔너리에서 평균 점수를 계산하는 코드를 작성하세요.
scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}
여기에 평균을 계산하는 코드를 작성하세요
"""
scores = {"국어": 85, "영어": 90, "수학": 78, "과학": 92}
avg = sum(scores.values()) / len(scores)
print(avg)

# 14번
"""
문자열에서 공백을 제거하고 모두 소문자로 변환하는 코드를 작성하세요.
입력 문자열은 "Python Programming"이며, 결과는 "pythonprogramming"이 되어야 합니다.
"""
a = input()
b = a.replace(" ", "").lower()
print(b)

# 15번
"""
1부터 사용자가 입력한 숫자까지의 합을 계산하는 프로그램을 작성하세요.
단, 3의 배수는 제외하고 합을 계산합니다.
"""
user = int(input())
count = 0
for i in range(1, user + 1):
    if i % 3 != 0:
        count += i
print(count)