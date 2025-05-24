# set : 집합 -> 리스트, 튜플과 다르게 순서가 없고(인덱싱, 슬라이싱 불가능), 중복된 값 허용X


# 셋 메서드는 dir()함수를 통해 어떤 메서드, 속성이 있는지 알 수 있다
print(dir(set))
"""
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'] 출력
"""


# set 집합
z = set([1, 2, 3, 3, 3])
print(z)  # {1, 2, 3} 출력


# 합집합(|)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5} 출력


# 교집합(&)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 & set2)  # {3} 출력


# 차집합(-)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 - set2)  # {1, 2} 출력


# add() : 집합에 원소 추가
set1 = {1, 2, 3}
set1.add(4)
print(set1)  # {1, 2, 3, 4} 출력


# clear() : 집합의 모든 원소 제거
set1 = {1, 2, 3, 4}
set1.clear()
print(set1)  # set() 출력


# copy() : 집합 복사본 반환
set1 = {1, 2, 3}
set2 = set1.copy()
print(set2)  # {1, 2, 3} 출력


# remove() : 특정 원소 제거, 해당 원소가 집합에 없으면 KeyError 발생
set1 = {1, 2, 3, 4}
set1.remove(3)
print(set1)  # {1, 2, 4} 출력


# discard() : 특정 원소 제거, 해당 원소가 집합에 없어도 에러 발생 하지 않음
set1 = {1, 2, 3, 4}
set1.discard(5)
print(set1)  # {1, 2, 3, 4} 출력