# 시퀀스 자료형 (인덱싱, 슬라이싱 가능)
# 튜플 : ()로 표현 -> 수정 불가능 -> 데이터의 안정성, 처리속도의 측면에 장점


# 리스트 메서드는 dir()함수를 통해 어떤 메서드, 속성이 있는지 알 수 있다
print(dir(tuple))
"""
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index'] 출력
"""


# 튜플 내에서 특정 값이 나타나는 횟수 반환
a = (1, 2, 3, 4, 3, 5)
print(a.count(3))  # 2 출력


# 특정 값이 튜플 내에서 처음으로 나타나는 위치의 인덱스 반환
a = (1, 2, 3, 4, 3, 5)
print(a.index(3))  # 2 출력