# 시퀀스 자료형이 아님 (인덱싱, 슬라이싱 불가능)
# 딕셔너리 : {}로 표현 -> 키(key)와 그에 해당하는 값(value)로 이루어져있다


"""
▷ 딕셔너리 생성법 : key값은 중복 안 된다◁
변수 = {'key1' : 'value1', 'key2' : 'value2'}
또는 dict([('key1', 'value1'), ('key2', 'value2')])
또는 dict(key1 = 'value1', key2 = 'value2')
"""


# 딕셔너리 메서드는 dir()함수를 통해 어떤 메서드, 속성이 있는지 알 수 있다
print(dir(dict))
"""
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'] 출력
"""


# 딕셔너리 항목 변경
person = {"name": "licat", "age": 25}
person["name"] = "lubi"
person["age"] = 20
print(person)  # {'name': 'lubi', 'age': 20} 출력


# 딕셔너리 항복 추가
person = {"name": "licat", "age": 25}
person["city"] = "ulsan"
print(person)  # {'name': 'licat', 'age': 25, 'city': 'ulsan'} 출력


# zip() : 두 리스트를 서로 짝짓는 함수 / dict() : 그 짝을 딕셔너리로 바꿔준다
keys = ["name", "city", "job"]
values = ["lubi", "busan", "student"]
print(dict(zip(keys, values)))
# {'name': 'lubi', 'city': 'busan', 'job': 'student'} 출력


# clear() : 딕셔너리의 모든 키-값 쌍을 삭제
data = {"name": "licat", "city": "busan", "age": 25}
data.clear()
print(data)  # {} 출력 / print(data.clear())는 clear()의 반환값 None을 출력


# copy() : 딕셔너리 복사
person = {"name": "licat", "city": "Jeju", "job": "Developer"}
copy_person = person.copy()
print(copy_person)


# fromkeys() : 시퀀스 자료형(리스트, 튜플)을 기반으로 딕셔너리 생성 가능
keys = ["name", "city", "job"]
value = None
## 키만 생성 가능 value는 ['licat', 'Jeju', 'Developer'] 이렇게 생성 X
print(dict.fromkeys(keys, value))
# {'name': None, 'city': None, 'job': None} 출력


# get() : 딕셔너리에서 에러없이 값을 추출할 때 사용, 해당 키가 없으면 None 출력
## a.get('key', 'default(선택입력)') -> key값을 찾을건데, 없으면 default값 출력
numbers = {"one": "하나", "two": "둘", "three": "셋"}
print(numbers.get("one"))  # 하나 출력
print(numbers.get("four"))  # None 출력
print(numbers.get("four", "4"))  # 4 출력


# items() : 딕셔너리의 키와 값을 쌍으로 추출할 때 사용, 결과는 dict_items로 반환
## 이 객체에서 인덱싱할라면 list로 변환해서 인덱싱
person = {"name": "licat", "city": "Jeju", "job": "Developer"}
print(person.items())
# dict_items([('name', 'licat'), ('city', 'Jeju'), ('job', 'Developer')]) 출력


# pop(key값) : 주어진 키 값 반환, 해당 키-값 쌍을 딕셔너리에서 삭제
numbers = {"one": "하나", "two": "둘", "three": "셋"}
print(numbers.pop("one"))  # 하나 출력
print(numbers)  # {'two': '둘', 'three': '셋'} 출력


# popitem() : 딕셔너리의 마지막 키-값 쌍을 반환, 그 항목 삭제
numbers = {"one": "하나", "two": "둘", "three": "셋"}
print(numbers.popitem())  # ('three', '셋') 출력
print(numbers)  # {'one': '하나', 'two': '둘'} 출력


# update() : 데이터 추가, 병합
numbers = {"one": "하나", "two": "둘", "three": "셋"}
numbers.update({"four": "넷", "five": "다섯"})
print(numbers)
# {'one': '하나', 'two': '둘', 'three': '셋', 'four': '넷', 'five': '다섯'} 출력