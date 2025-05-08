'''
짜장과 짬뽕을 선택한다.
짜장을 선택한다(불짜장,간짜장,쟁반짜장)
->중첩반복문을 사용해서 쟁반짜장 문자열이 들어간 친구만
"쟁반짜장"이라고 출력
짬뽕을 선택한다. -> 짬뽕 문자열을 출력
'''
# a = input()
# if a == "짜장":
#     if "쟁반짜장" in b:
#         print("쟁반짜장")
#     else:
#         print("메뉴에 없습니다.")
# elif a == "짬뽕":
#     print("짬뽕")
a = input()
if a.find("짜장") != -1:
    if "쟁반" in a:
        print("쟁반짜장")
elif a == "짬뽕":
    print("짬뽕")

a = [1, "2", "good1", 4, [1, 2, 3, [123, "good"],31],2]
# 1. good이라는 문자열을 인덱싱 기법으로 추출
# 2. 슬라이싱 기법을 통해 [123,"good"] 을 추출
print(a[4][3][1])
print(a[4][3][0:2])

# 리스트
## 후입선출(Last In First Out(LIFO))
## a = b a.append(123) print(b)를 하면 a와 b 값이 동일해지기 때문에
## 복제 할 때는 copy()를 쓴다
## 다 지울 때는 clear()를 쓴다.
"""
1. 빈리스트를 만든다.
2. append를 사용하여 이중 리스트를 만든다.
3. 출력한다.
4. 리스트의 데이터를 다 지운다.
5. 출력한다.
6. copy를 활용한다.
7. 카피를 활용한 리스트에 append를 사용하여 출력한다.
"""
# 1
a = []
# 2
a.append([1, 2, 3, [4, 5]])
# 3
print(a)
# 4
a.clear()
# 5
print(a)
# 6
a = [1, 2]
b = a.copy()
# 7
b.append("hee")
# 8
print(b)

# count()
a = [1, 2, 3, "okay", 1, 1 ,1]
print(a.count(1)) # 4출력

b = [1, 2, 3, [1, 2, 3, 1]]
print(b.count(1)) # 1출력 <b의 [1, 2, 3, 1]은 한 묶음으로 쳐서>

a = [1, 2, 3, [1, 2, 3, 1]]
print(a[2], a[3][2])
print(a.count(1) + a[3].count(1))
'''
*포맷(정렬)키
Windows : Shift + Alt + F
macOS : Shift(⇧) + Option(⌥) + F
Linux : Ctrl + Shift + I
'''

# extend(확장)
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a.extend(b) # [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
c = 'good'
b.extend(c) # [5, 6, 7, 8, 'g', 'o', 'o', 'd']
print(b)

a = ["good", "okay"]
'''
b = a.index("aaaa")
print(b) # 에러뜸 <문자열 인덱스는 find를 쓰지 못함>
'''
b = a.index("okay")
print(b)