"""
*5/10일 토요일 과제 6문제*
1. 사용자로부터 입력받은 정수 두 개를 더한 결과를 출력하세요
2. 문자열을 입력받아 거꾸로 출력하세요 ex)입력받은 문자가  'python so bad' -> 출력 결과는  'dab os nohtyp'
3. 숫자를 입력 받아 짝수면 'Even', 홀수면 'Odd'를 출력하세요
4. [1, 2, 3, 4, 5]의 평균을 구하세요
5. 두 리스트를 입력받아 교집합을 출력하세요
6. 튜플 (1, [2, 3], 4)에서 리스트 요소 3을 100으로 바꾸세요
"""

# 1번
a, b = int(input()), int(input())
print(f"두 숫자의 합은 : {a + b}")

# 2번
a = input()
print(a[::-1])

# 3번
a = int(input())
if a % 2 == 0:
    print("Even")
elif a % 2 == 1:
    print("Odd")

# 4번
a = [1, 2, 3, 4, 5]
avg = sum(a) / len(a)
print(avg)

# 5번
# 문자열을 정수로 변환
a, b = list(map(int, input().split())), list(map(int, input().split()))
c = list(set(a) & set(b))
print(f'교집합 : {c}')

# 6번
a = (1, [2, 3], 4)
a[1][1] = 100
print(a)