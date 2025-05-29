'''
1번 : 홀수의 평균 구하기,
정수 n 이 주어질 때, n 이하의 홀수들의 평균을 구해서 return 하도록 solution 함수를 완성하세요.
[ 조건 ]
n은 1 이상의 자연수,
평균은 소수점 이하 첫째 자리까지 출력(소수점 자리 반올림),
[ 풀이 방식 ]
리스트 컴프리헨션과 sum()/ len()을 이용하여 구하기
'''
def solution(n):
  # num = []
  # for i in range(1, n + 1):
  #   if i % 2 != 0:
  #     num.append(i)
  # 위 코드를 컴프리헨션으로 바꾼 코드
  # 1부터 n까지 홀수 찾기
  num = [i for i in range(1, n + 1) if i % 2 != 0]
  # 홀수가 없는 경우 처리
  if len(num) == 0:
    return 0
  avg = sum(num) / len(num)
  return avg

n = 10
print(solution(n))


'''
2번 : 최고 점수 학생 찾기,
학생 이름과 점수가 담긴 딕셔너리 scores가 주어질 때, 가장 점수가 높은 학생의 이름을 return 하도록 solution 함수를 완성하세요.
[ 조건 ]
딕셔너리의 key는 문자열(이름), value는 정수(점수),
최고 점수를 받은 학생이 여럿일 경우 아무나 리턴,
[ 풀이 방식 ]
max() 함수와 lambda를 사용하여 구하기
'''
def solution(scores):
  stud = max(scores.items(), key=lambda x: x[1])
  return stud[0]
# 예시
scores = {"철수": 85, "영희": 92, "민수": 78, "영지": 88}
print(solution(scores))