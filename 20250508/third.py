# reverse() 뒤집기
## b = a.reverse() <X> b라는 변수에 reverse를 받아도 reverse 행동은 수행하지만 값이 없다(None)
## b = a.reverse() -> None 형태
## b = a.pop(1) -> a에서 pop으로 추출된 int값이 b의 값으로 들어간다
a = [1, 2, 3, 4, 5]
a.reverse()  # <O> [5, 4, 3, 2, 1] 출력 / 원본을 건드리는거랑 마찬가지라서 권장하지 않는다
print(a)

# ☆☆reversed()☆☆ -> 원본 훼손 x, 뒤집는다 (파이썬에서 기본적으로 제공하는 함수)
a = [1, 2, 3, 4, 5]
b = list(reversed(a))  # 리스트를 형변환해준다
## print(reversed(a)) -> <list_reverseiterator object at 0x00000236D1A25B40> 출력
print(a)
print(b)

# sort / sorted (오름차순)
a = [5, 4, 3, 2, 1]
"""
a.sort()
print(a)
-> 원본 훼손
"""
b = list(sorted(a))  # 원본데이터 복사 후 정렬 -> 리스트 타입으로 변경
print(a)
print(b)
## sorted(리스트, reversed=bool)
c = [1, 2, 3, 4, 5]
## reversed와 다르게 sorted는 특정 타입이 없는 그냥 기능이기 때문에 list를 안써도 된다
sorted(c, reverse=False) # reverse=Flase 뒤집는거의 반대 ==> sorted(a)와 같다
d = sorted(c, reverse=True) # 내림차순 정렬
print(d)