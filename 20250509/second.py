# 딕셔너리 <키(key):값(value)> dict()
## 인덱싱, 슬라이싱 불가능 / 단, set과 다르게 순서는 보장
my_dict = {"me": "희현"}
my_dict2 = dict()
"""
이렇게도 작성 가능
my_dict2 = dict([("one","하나"),("two","둘")])
->키가 두개 (튜플 기준으로 함)
"""
my_dict3 = {"me": [1, 2, 3], "me2": "good"}
print(my_dict)

## 딕셔너리(dict) 데이터 추가 (Create)
dict4 = dict()
# max가 (key), 김승주 강사님이 (값)
dict4["max"] = "김승주 강사님"
print(dict4)
# ex)
dict5 = dict()
dict5["age"] = 27
dict5["b"] = (3, 27, 18)
dict5["from"] = "busan"
dict5["a"] = [0, 1, "sim"]
print(dict5)

## 딕셔너리(dict) 데이터 읽기 (Read)
person = {"name": "licat", "age": 25, "height": 165.5}
print(f"이름 : {person['name']} 입니다.")
print(f"나이 : {person['age']} 입니다.")

## 딕셔너리(dict) 데이터 수정 (Update)
person["age"] = 30
print(person)
# ex)
person["name"] = "lubi"  # 수정
person["weight"] = 1  # 추가
print(person)

## 딕셔너리(dict) 데이터 삭제 (Delete)
del person["height"]
print(person)
person["age"] = None  # 키를 남기고 값을 없애고 싶을 때 사용
print(person)
# ex) 리스트 안에 일부를 지우고 싶을 때
a = {"good": ["a", "b", "c"]}
a["good"].remove("c")
print(a)
# ex) b = {"good1": {"good2": [1, 2, 3, [1, 2, 3, 4]]}}로 바꾸기
b = {"good1": {"good2": [1, 2, 3, [1, 2, 3]]}}
b["good1"]["good2"][3].append(4)
print(b)

# get(키, 키가 없을 경우의 value)
## city = person["city2"] -> key error 뜸
## 에러를 방지하면서 default값을 정해줌
## 내가 찾는 키가 없을 때 대체 값으로 아무거나 정하는 것을 get이라고 한다
person = {"name": "licat", "age": 25, "city": "Ulsan"}
city = person.get("city", "없음")
print(city) # Ulsan 출력
city2 = person.get("city2", "없음")
print(city2) # 없음 출력

# 키(key)만 가지고 오고 싶을 때
person = {"name": "licat", "age": 25, "city": "Ulsan"}
person_keys = person.keys()
print(person_keys) # dict_keys(['name', 'age', 'city']) 출력
## dict_keys(['name', 'age', 'city'])를 리스트로 변경
## dict_keys : 특정 기능을 가지고 있다 
a = list(person_keys) # 리스트로 형변환
print(a)

# 값(value)만 가지고 오고 싶을 때
person = {"name": "licat", "age": 25, "city": "Ulsan"}
person_values = person.values()
print(list(person_values)) # 리스트로 형변환

# 전체를 가지고 오고 싶을 때
person = {"name": "licat", "age": 25, "city": "Ulsan"}
person_items = person.items()
print(list(person_items)) # 리스트로 형변환
## del person["age"] / person.pop("age") 제거하는건 같다
## person.pop("age")를 더 권장
## ex) a = person.pop("age") age라는 키에 있는 값을 a에 저장