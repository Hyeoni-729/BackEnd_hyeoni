# 튜플 복습
a = (1, 10, 1, 2, 3)
## 슬라이싱
b = a[2:5]  # (1, 2, 3)추출
c = a[1]  # (10)
## 기능
c = a.count(1)  # 2
d = a.index(1)  # 0 <처음 1이 나오는 위치만 반환>

# 자료구조 set <가장 큰 특징 : 순서 보장 X, 중복 허용 X>
## 문제에서 '중복을 제거해라' 가 있으면 set 사용
"""set은 인덱스 기능이 안 먹힌다.
a = {1,2,3}
print(a[0]) # TypeError: 'set' object is not subscriptable
"""
a = {1, 2, 3, 1}
print(a)  # {1,2,3}출력
print(len(a))  # 3
## 형변환 <list -> set>
a = [1, 1, 1, 2, 2, 3]
## a에 있는 값 중 중복된 값을 지운다.
b = set(a)
print(b)
## c = list(b) -> <set -> list>

"""
set은 합집합 (|), 교집합 (&), 차집합(-) 부호 사용
"""
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"합집합 : {set1 | set2}")  # 합집합 : {1, 2, 3, 4, 5, 6, 7, 8}
print(f"교집합 : {set1 & set2}")  # 교집합 : {4, 5}
print(f"차집합 : {set1 - set2}")  # 차집합 : {1, 2, 3}
print(f"차집합 : {set2 - set1}")  # 차집합 : {8, 6, 7}
print(f"대칭 차집합 : {set1.symmetric_difference(set2)}")
print(f"set1이 set2의 부분집합인가? : {set1.issuperset(set2)}")

## set은 수정이 가능
fruits = {"apple", "banana", "cherry"}
""" set의 추가 명령어 -> add() """
fruits.add("orange")
print(fruits)
""" set의 제거 명령어 -> remove() """
fruits.remove("apple")
print(fruits)