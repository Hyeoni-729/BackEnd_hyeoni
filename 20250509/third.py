# 반복문 (for ~ in ~ :)
## for 뱐수명 in 순회가능한객체:
s = "hello"
for j in s:
    print(j)
a = [1, 2, 3, 4, 5, 6]
for i in a:
    print(i)
## range : 범위 <0부터 숫자-1 까지의 범위 출력
## range(시작, 끝, 단계)
for i in range(5000):  # (0~4999 => index와 같다)
    print(i)
## ex) range(10, 51) -> 10부터 50까지의 범위 출력
for i in range(10, 51):
    print(i)
## ex) range(1, 11, 2) -> 1부터 10까지 2계단씩 점프해서 출력
for i in range(1, 11, 2):
    print(i)
## ex) 내림차순(음수 출력) -> 10부터 -11까지 -1계단씩 아래로 출력
for i in range(10, -11, -1):
    print(i)
"""
*간단실습
1. 1부터 100까지 출력
2. 2부터 50까지 짝수만 출력
3. 10부터 -1까지 출력
"""
# 1
for i in range(1, 101):
    print(i)
# 2
for j in range(2, 51, 2):
    print(j)
# 3
for k in range(10, -2, -1):
    print(k)

# 중첩 반복문
## ex) 1부터 99까지 3의 배수만 출력한다.
for i in range(1, 100):
    if i % 3 == 0:
        print(i)
## ex) 구구단 만들기
# i(2~9)는 고정 j(1~9)는 9번 회순 <총 72번 반복>
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
        if i * j == 9: # i * j가 9라면 9출력
            print(9)