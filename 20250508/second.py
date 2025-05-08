# insert() 삽입
## insert(인덱스(위치), 값)
## 비용이 많이 든다
## insert는 끼어들기 append는 맨 뒤에 붙이기
a = [1, 2, 3, 4, 5]
# 0, 1, 2, 3, 4, 5를 만들려면
a.insert(0, 0)
print(a)

# pop()
## 제일 끝에 있는 값 추출
## 리스트 값이 비어있으면 IndexError: pop from empty list 오류 뜸
a.pop()
print(a)
## 미연에 방지하려면
if len(a) >= 1: # 리스트 내부의 데이터 갯수가 1개 이상이라면 추출
    a.pop()
else: # 아니면 print
    print('리스트가 비어있습니다.')

# remove()
## remove(값)
## remove는 왼쪽 부터 한개의 remove명령어 당 하나씩 지운다
a = [1, 2, 3, 1, 1]
a.remove(1)
print(a) # [2, 3, 1, 1]
a.remove(1)
print(a) # [2, 3, 1]
a.remove(50) # ValueError: list.remove(x): x not in list 오류뜸

"""
1. 기존에 데이터가 있는 리스트를 만든다.
2. insert를 활용해서 데이터를 넣는다.
3. pop을 사용하여 꺼낸 데이터를 출력한다.
4. remove를 사용하여 특정 데이터를 제거해본다.
"""
# 1
a = [1, 2, "딸기빙수", 4]
# 2
a.insert(2, "망고빙수")
print(a)
# 3
a.pop()
print(a)
# 4
a.remove("딸기빙수")
print(a)