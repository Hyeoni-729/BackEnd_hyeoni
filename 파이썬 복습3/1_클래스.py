# 파이썬 복습2에 1_클래스.py랑 연결
# 매직 메서드
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __mul__(self, other):
    return 'hello'
  
dot1 = Point(10, 20)
dot2 = Point(20, 30)
print(dot1 * dot2) # hello 출력

'''
매직 메서드 종류
1. __init__(self, ...) : 객체가 생성될 때 호출되는 생성자 메서드
2. __str__(self) : str() 함수 출력 결과와 같다
3. __add__(self, other) : 덧셈연산
4. __sub__(self, other) : 뺄셈연산
5. __mul__(self, other) : 곱셈연산
6. __truediv__(self, otehr) : 나눗셈연산
7. __eq__(self, other) : 동등연산(==)
8. __ne__(self, other) : 부등연산(!=)
9. __lt__(self, other) : "작다"연산(<)
10. __le__(self, other) : "작거나 같다"연산(<=)
11. __gt__(self, other) : "크다"연산(>)
12. __ge__(self, other) : "크거나 같다"연산(>=)
'''

