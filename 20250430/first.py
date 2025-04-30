a = 10
b = 21
if a > 10:
    print("good")
elif b == 20:
    print("20입니다")
elif a == 10:
    print("10입니다")
else:
    print("아무것도 아니다")

'''
split() 활용, a, b 변수를 활용해 키, 몸무게 입력받기
키와 몸무게를 나눈 나머지 출력하기
조건문을 활용해서 키가 130 이상이면 A, 150 이상이면 B,
170 이상이면 C, 180 이상이면 D를 출력하기
'''
a, b = input().split()
a, b = int(a), int(b)
# a, b = map(int, input().split()) 으로 한 줄 작성 가능
print(a % b)
if a >= 180:
    print("D")
elif a >= 170:
    print("C")
elif a >= 150:
    print("B")
elif a >= 130:
    print("A")

# and / or 연산활용
a = 10
b = 20
if a == 10 and b == 20:
    print("True")
else:
    print("False")

'''
a, b, c입력받고 a가 100이고 b가 200이상이면 A출력
b가 1이면 B출력 아무것도 해당x면 C출력
'''
a, b, c = map(int, input().split())
if a == 100 and b >= 200:
    print("A")
elif b == 1:
    print("B")
else:
    print("C")

'''
1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
같은 눈이 3개가 나오면 10,000원+(같은 눈) ×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) ×100원의 상금을 받게 된다.
3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
'''
# 내 풀이
a, b, c = map(int, input().split())
if a == b == c: # 같은 눈이 3개일 경우
    print(10000 + a * 10)
elif a == b or a == c: # 같은 눈이 2개일 경우
    print(1000 + a * 100)
elif b == c: # 같은 눈이 2개일 경우
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)

# 다른 풀이
a, b, c = map(int, input().split())
if a == b == c: # 같은 눈이 3개일 경우
    price = 10000 + a * 10
elif a == b or a == c: # 같은 눈이 2개일 경우
    price = 1000 + a * 100
elif b == c: # 같은 눈이 2개일 경우
    price = 1000 + b * 100
else:
    price = 0 # 혹시 모를 최댓값 유무 때문에 0으로 초기화
    # price = 0 문장이 없으면 price = temp * 100 에서 오류뜸
    # 출력할 때 모두 참이 아니면 price 의 값이 없으니까 임의로 price의 값을 0으로 둔다. (값이 없으면 오류가 뜨니까.)
if a != b and b != c and a != c: # 모두 다른 눈일 때 최댓값 찾기
    temp = a
    if b > temp:
        temp = b
    if c > temp:
        temp = c
    price = temp * 100
print(f"상금 : {price}원")