# break문
"""break구문은 바로 위의 반복문만 탈출"""
# x가 5일때 까지만 출력
x = 0
while x < 10:
    print(x)
    if x == 5:
        break
    x += 1

# j가 6일때 부터는 중단 (i * 5)
for i in range(2, 10):
    for j in range(1, 10):
        if j > 5:
            break
        print(f"{i} * {j} = {i * j}")


# continue, pass
"""
continue구문은 반복문이 실행하는 코드 블록의 나머지 부분을 실행하지 않고 다음 반복으로 건너가게 흐름을 조정"""
"""
pass구문은 아무런 동작을 하지 않고 다음 코드를 실행, 에러가 나지 않도록 해주는 역할"""
## continue
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)  # 1 2 4 5 출력

## pass
x = 0
while x < 5:
    x += 1
    if x == 3:
        pass
    print(x)  # 1 2 3 4 5 출력


'''반복문 연습문제'''
# 1. 재고가 1개 남았을 때 반복문은 멈추어야 합니다. 아래의 코드를 완성하여, 5마리의 고등어부터 1마리의 고등어까지 재고를 표시
for i in range(5, 0, -1):
    print('고등어', i, '개 남음')
    if i == 1:
        break