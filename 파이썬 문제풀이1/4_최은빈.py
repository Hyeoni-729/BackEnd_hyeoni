'''
1번 : 짝수의 합
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
(두 가지 방법을 사용해서 풀어보세요.)
1) 반복문 사용
2) sum()과 range() 사용 
Q. 어떤 방법이 메모리를 더 아낄 수 있을까?
-> 방법 2
'''
# 1) 반복문
def solution(n):
  result = 0
  for i in range(1, n + 1):
    if i % 2 == 0:
      result += i
  return result

# 2) sum()과 range() 사용
def solution2(n):
  return sum(range(2, n + 1, 2))


'''
2번 : 중복된 숫자 개수
정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.(두 가지 방법을 사용해서 풀어보세요.
1) count 사용 
2) Counter사용 
Q. count와 Counter는 모두 데이터 안에 있는 값의 개수를 셀 수 있어. 그렇다면 각각 어떤 상황에서 써야 메모리를 더 아낄 수 있을까?
-> 단순히 하나의 값만 세는 경우라면 count()가 메모리를 더 아낍니다. 하지만 여러 값들을 조회해야 한다면 Counter가 전체적으로 더 효율적
'''
# 1) count 사용
def solution3(array, n):
  return array.count(n)

# 2) counter 사용
def solution4(array, n):
  counter = counter(array)
  return counter[n]