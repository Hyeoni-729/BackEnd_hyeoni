# 1. 문자를 사용자에게 입력받고, 그 문자를 2번 출력하는 프로그램
a = input()
print(a * 2)


# 2. 문자열 s에 마지막에 있는 문자열을 2번 더 붙이는 코드
s = 'jun'
print(s + s[-1]*2)


# 3. 'abcde', 숫자, 대쉬(-), 언더스코어(_)를 모두 제거해라
s = 'hello_world123'
remove_s = 'abcde0123456789-_'
a = ''
# s의 각 문자를 하나씩 확인
for char in s:
  # 만약 그 문자가 제거할 문자가 아니라면
  if char not in remove_s:
    # 결과 문자열에 추가
    a += char
print(a)


# 4. 확장자를 출력해주는 코드를 작성해주세요. 확장자는 png, jpeg, mp4 등입니다
s = 'licat.jpeg'
a = 'licat.png'
print(s.split('.')[-1])
print(a.split('.')[-1])