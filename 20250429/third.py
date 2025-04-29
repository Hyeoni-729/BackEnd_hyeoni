# if조건문
## 예약어 if는 변수로 쓸 수 없다.
age = 10
height = 200
if age > 18 and height >= 150:
    print("성인입니다")
elif age == 10 and height < 140:
    print("동갑")
elif age >= 4 or height >= 150:
    print("거인")
else:
    print("미성년자")
# 거인 출력
print("프로그램 종료")

'''
if 입력한 비밀번호 != 입력한비밀번호 확인:
    회원가입 거부
'''

# ex)한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
# 년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)
yyyy, mm, dd = input().split()
'''
birth = input()
yyyy, mm, dd = birth.split() 도 된다(map형식)
'''
yyyy, mm, dd = int(yyyy), int(mm), int(dd)

if yyyy % 2 == 0:
    print("짝수년도에 태어났습니다.")
else:
    print("홀수년도에 태어났습니다.")