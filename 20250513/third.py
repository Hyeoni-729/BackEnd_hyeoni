# filter
result = 0
for i in range(1, 11):
    if i % 2 == 0:
        result += i
print(result)

## filter 문제
# 항공사, 편명, 좌석번호, 이름, 나이, 짐무게(kg), 마일리지
data = [
    ['대한항공', 'KE607', '12A', '김민준', 42, 23, 5280],
    ['아시아나', 'OZ721', '8C', '이', 29, 18, 3450],
    ['제주항공', '7C101', '15F', '박지민', 35, 15, 720],
    ['진에어', 'LJ211', '4D', '최서우미래한별', 51, 27, 8900],
    ['에어부산', 'BX213', '21B', '정', 24, 12, 1250],
    ['티웨이', 'TW305', '19E', '강민석', 38, 20, 2760],
    ['에어서울', 'RS808', '3C', '윤지현', 47, 16, 4320],
    ['대한항공', 'KE123', '7F', '송', 33, 21, 6780],
    ['아시아나', 'OZ562', '11D', '장하은별님달빛', 26, 19, 1890],
    ['제주항공', '7C505', '17B', '황수진', 40, 14, 940]
]
"""1번 : 나이가 30살 이상인 사람들을 뽑아서 출력"""
def f(x):
    return x[4] >= 30
for i in filter(f, data):
    print(i)

"""2번 : 편명과 이름으로 된 새로운 리스트를 만들어라."""
def f(x):
    return [x[1], x[3]]
print(list(map(f, data)))

"""3번 : 30살 이상인 사람들의 나이 합을 구해라
30살 이상인 사람을 filter 해서 나이를 다 더해라"""
# 방법1 : 나이만 map해서 추출, filter로 30살 이상인 사람 추출해서 sum
# 방법2 : filter로 30살 이상인 사람 추출한 다음 map으로 나이만 뽑고 sum

# 방법1 소스
def f(x):
    return x[4]
def ff(x):
    return x >= 30
sum(list(filter(ff, map(f, data))))

# 방법2 소스
def f(x):
    return x[4] >= 30
def ff(x):
    return x[4]
map(ff, filter(f, data))
# sum(list(map(ff, filter(f, data)))) 은 절대 쓰면 안된다"""

"""4번 : 짐무게가 20kg 이상인 승객들의 마일리지 평균을 구해주세요"""
# 문제1 <가독성 좋은 코드>
def f(x):
    return x[5] >= 20
def ff(x):
    return x[6]
filtering_data = list(map(ff, filter(f, data))) # list -> 메모리 효율 떨어짐
print(sum(filtering_data) / len(filtering_data)) # sum -> 한 번 더 순회 돌아야해서 메모리 효율 떨어짐

# 문제1 <효율성 좋은 코드>
def f(x):
    return x[5] >= 20
def ff(x):
    return x[6]
count = 0
sum_result = 0
for i in map(ff, filter(f, data)):
    count += 1
    sum_result += i
print(sum_result / count)

"""5번 : 아시아나 항공을 이용하는 40세 미만 승객들의 이름 길이 합을 구해주세요"""
def f(x):
    return x[0] == '아시아나' and x[4] < 40
def ff(x):
    return x[3]
print(len(''.join(map(ff, filter(f, data)))))

# enumerate
list(enumerate('hello'))
list(enumerate('hello', 100))
for i in enumerate('hello'):
    print(i)

for index, value in enumerate('hello'):
    print(i)

for i, v in enumerate('hello'):
    print(i)

for i in range(len('hello')): # 이래 쓸거면
    print(i)

for i, _ in enumerate('hello'): # 이래 쓰는 것을 권장
    print(i)

# len
len([10, 20, 30])
# format
format(10, 'b')
format(10000000, ',') # 굉장히 많이 쓰임
# input
input('입력하세요!') # 주의할 점 : 숫자를 입력해도 문자로 입력받는다.

# range
## range는 리스트가 아니라 range타입이다.

# map(함수, iterable)
## map은 어떤 데이터를 '추출'할 때 많이 사용한다.
def f(x):
    return x ** 2
list(map(f, [1, 2, 3, 4]))