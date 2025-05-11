"""
*5/11일 일요일 과제 5문제*
1. ID와 비밀번호를 입력받고, 다음과 같은 조건이면 로그인 성공이라고 출력
- ID가 "admin" 또는 "user"
- 비밀번호는 "1234"
2. 비밀번호를 입력받아, 다음 조건을 모두 만족하면 "유효한 비밀번호" 출력
- 8자 이상
- "!" 또는 "#" 기호가 포함되어 있음
3. 정수 N을 입력받아 아래와 같은 별 피라미드 출력
ex) N = 3
*
**
***
4. 딕셔너리 값을 기준으로 내림차순으로 정렬한 리스트를 출력하세요
5. 구구단 2단부터 9단까지 for문으로 작성해서 출력하세요
"""

# 1번
user, pw = input(), input()
if (user == "admin" or user == "user") and pw == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")

# 2번
pw = input()
if len(pw) >= 8 and ("!" in pw or "#" in pw):
    print("유효한 비밀번호")
else:
    print("유효하지 않음")

# 3번
a = int(input())
for i in range(1, a + 1):
    print("*" * i)

# 4번
a = {"a": 3, "b": 1, "c": 2}
b = sorted(a.items(), key=lambda x: x[1], reverse=True)
print(b)

# 5번
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}*{j} = {i*j}")