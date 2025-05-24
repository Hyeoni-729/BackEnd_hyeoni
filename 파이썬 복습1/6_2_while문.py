# while문
## 조건이 참일 때까지 반복할 때, 무한 반복 할 때 사용

# 쉘 프로그래밍 : 사용자의 명령어를 해석, OS가 수행할 수 있도록 지시
import os

while True:
    userinput = input(">")
    if userinput == "pwd":
        # print(현재위치 출력)
        print(os.getcwd())
    elif userinput == "dir" or userinput == "ls":
        # print(현재 폴더에 폴더와 파일명 출력)
        print(os.listdir(os.getcwd()))
    elif userinput == "exit":
        print("안녕히가세요")
        break


# 업, 다운 게임 : random -> 난수 생성 모듈
import random

answer = random.randint(1, 1000)
while True:
    userinput = int(input("숫자를 입력하세요 : "))
    if userinput > answer:
        print("Down")
    elif userinput < answer:
        print("Up")
    else:
        print("정답!")
        break


# 구구단 (2 ~ 9단)
i = 2
while i < 10:
    j = 1
    while j <10:
        print(f'{i} * {j} = {i * j}')
        j += 1
    i += 1

# 구구단 (2단 만)
i = 2
j = 1
while i < 10:
    while j < 10:
        print(f'{i} * {j} = {i*j}')
        j += 1
    i += 1