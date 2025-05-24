# 시퀀스 자료형 (인덱싱, 슬라이싱 가능)
# 리스트 : []로 표현 -> 수정 가능<CRUD : Creat Read Update Delete>


# 별표(*)를 이용한 언패킹
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)  # 1 [2, 3, 4] 5 출력


# 다양한 슬라이싱 형태 알아보기
l = [1, 2, 3, 4, 5]
print(l[:])  # 처음부터 끝까지 출력
print(l[::-1])  # 처음부터 끝까지 반대로 출력(=reverse)
print(l[::2])  # 처음부터 두 번 점프 한 결과만 [1, 3, 5] 출력
print(l[0:4][::-1])  # 0번부터 3(4-1)번까지 역순으로 [4, 3, 2, 1] 출력


# 리스트 메서드는 dir()함수를 통해 어떤 메서드, 속성이 있는지 알 수 있다
print(dir(list))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] 출력
"""


# 리스트의 끝에 값을 추가
a = [1, 2, 3]
a.append(10)
print(a)  # [1, 2, 3, 10] 출력


# 리스트의 모든 항목 제거
a.clear()
print(a)  # [] 출력


# 리스트의 복사(copy()를 쓰지 않으면 원본도 같이 훼손)
a = [1, 2, 3]
b = a.copy()
b[0] = 100
print(a, b)  # [1, 2, 3] [100, 2, 3] 출력
"""
-> 슬라이싱으로 copy와 동일한 출력 가능
l = [10, 20, 30]
ll = l[:]
l[0] = 100
print(l, ll) # [10, 20, 30] [100, 20, 30] 출력
"""


# 특정 값이 리스트에 몇 번 포함되어 있는지 갯수 구하기
a = [1, 1, 2, 3, 1]
print(a.count(1))  # 3 출력


# 리스트에 다른 리스트나 항목들 추가
a = [1, 2, 3]
a.extend([4, 5, 6])
print(a)  # [1, 2, 3, 4, 5, 6] 출력
"""이렇게도 가능"""
l = [10, 20, 30]
l.extend("hello")
print(l)  # [10, 20, 30, 'h', 'e', 'l', 'l', 'o'] 출력


# 인덱스값 반환(리스트에는 find메서드가 없다)
a = [10, 20, 30, 40]
print(a.index(30))  # 2 출력


# 주어진 인덱스값에 값을 추가
a = [10, 20, 30, 40]
a.insert(2, 25)
print(a)  # [10, 20, 25, 30, 40] 출력


# 리스트의 특정 위치에 있는 값을 반환, 해당 값을 리스트에서 삭제
a = [10, 20, 25, 30, 40]
a.pop(1)
print(a)  # [10, 25, 30, 40] 출력
""".pop() 처럼 값을 넣지 않을 경우 마지막 값을 삭제"""


# 첫 번째로 발견되는 주어진 값을 삭제
a = [1, 2, 3, 1, 2]
a.remove(1)
print(a)  # [2, 3, 1, 2] 출력
"""위와 동일한 결과가 나오는 다른 방법"""
l = [1, 2, 3, 4, 2, 2, 1, 1]
print(list(filter(lambda x: x != 2, l)))  # [1, 3, 4, 1, 1] 출력


# reverse() / reversed()
## reverse() : 원본은 변경 O, 반환값은 없음(None)
a = [1, 2, 3, 1, 2]
print(a.reverse())  # None 출력
## reversed() : 원본은 변경 X, 리스트로 역순 반환
a = [3, 2, 5, 1, 4]
print(list(reversed(a)))  # [4, 1, 5, 2, 3] 출력


# sort() / sorted()
## sort() : 원본 리스트 오름차순으로 정렬, 반환값은 없음(None)
a = [3, 2, 5, 1, 4]
print(a.sort())  # None 출력
## sorted() : 원본은 변경 X, 새로운 리스트에 오름차순으로 정렬한 뒤 반환
a = [3, 2, 5, 1, 4]
print(sorted(a))  # [1, 2, 3, 4, 5] 출력
