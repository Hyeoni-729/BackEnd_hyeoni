# zip
## map, zip, filter는 변수로 할당하면 한 번 밖에 순회를 못 돈다.
## 왜냐하면 변수에서 다시 순회를 돌 수 있도록 초기화를 해줘야 하는데 초기화를 해주지 않는 함수라서.
a = [10, 20, 30]
b = (100, 200)
c = 'hello world'
print(list(zip(a, b, c)))

# iter, next
for i in range(10): # Stopiteration 오류가 뜰때까지 순회
    print(i)
s = 'hello'
ss = iter(s) # 이제 값을 순차적으로 꺼낼테니까 꺼낼 준비 해라.
print(next(ss)) # 다음 값을 꺼내라.

# 반복문(while)
## for ▶ 객체를 순회할 때
## while ▶ 정해진 수만큼 순회를 하거나, 무한 반복을 할 때
x = 0
while x < 10:
    print(x)
    x += 1 # 종료할 수 있는 연산

"""1번 : 1부터 100까지 짝수만 더하는 코드를 while문으로 작성"""
# 방법1 <별로인 코드>
x = 0
result = 0
while x < 101:
    if x % 2 ==0:
        result += x
    x += 1 # 종료할 수 있는 연산
print(result)

# 방법2 <위의 코드보다 좋은 코드>
x = 0
result = 0
while x < 11:
    result += x
    x += 2 # 종료할 수 있는 연산
print(result)

# 조건문(match)
day = '토'
match day:
    case "월" | "화" | "수" | "목" | "금":
        print("평일")
    case "토" | "일":
        print("주말")
    case _: # 매칭되지 않는것은 _ 넣는게 관례
        print("올바른 요일을 입력하세요")

# 이전에는 어떻게 사용했는가
today = '수'
day = {
    '월':'평일',
    '화':'평일',
    '수':'평일',
    '목':'평일',
    '금':'평일',
    '토':'주말',
    '일':'주말'
}
print(day.get(today, '제대로 입력하세요'))
# '제대로 입력하세요' -> default 값