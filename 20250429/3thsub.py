'''첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
'''
a, b = input().split()
a, b = int(a), int(b)
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

'''
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
'''
score = input()
score = int(score)
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

'''
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
'''
year = input()
year = int(year)
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")

'''
예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
'''
x, y = input(), input()
x, y = int(x), int(y)
if x > 0 and y > 0:
    print("1")
if x < 0 and y > 0:
    print("2")
if x < 0 and y < 0:
    print("3")
if x > 0 and y < 0:
    print("4")