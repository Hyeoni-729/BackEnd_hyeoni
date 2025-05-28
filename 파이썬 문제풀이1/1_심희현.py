"""
1번 : 학생 성적 관리 프로그램
딕셔너리 활용 : 학생 이름을 키(key), 점수를 값(value)으로 저장
리스트 컴프리헨션 대신 반복문 : 조건에 맞는 학생 필터링,
sorted() 함수 : key=lambda x: x[1]로 점수 기준 정렬, reverse=True로 내림차순,
enumerate() : 순위 매기기에 활용
* 주요 포인트:
sum(students.values())로 모든 점수의 합 계산
딕셔너리의 .items()로 (이름, 점수) 튜플 형태로 접근,
람다 함수 lambda x: x[1] 로 튜플의 두 번째 요소(점수) 기준 정렬
"""
def student_grade_manager():
    # 학생 데이터 초기화
    students = {}
    student_data = [("김철수", 85), ("이영희", 92), ("박민수", 78), ("최지영", 88)]
    # 1. 학생 추가
    for name, score in student_data:
        students[name] = score
    print("---학생 성적 관리 프로그램---")
    print(f"▷ 등록된 학생 : {students}")
    # 2. 전체 학생의 평균 점수 계산
    total = sum(students.values())
    avg = total / len(students)
    print(f"▷ 평균 점수 : {avg:.2f}점")
    # 3. 80점 이상인 학생들만 출력
    print("▷ 80점 이상인 학생")
    high = []
    for name, score in students.items():
        if score >= 80:
            high.append((name, score))
    # 점수 순으로 정렬(내림차순)
    high.sort(key=lambda x: x[1], reverse=True)
    for name, score in high:
        print(f"- {name} : {score}점")
    # 4. 점수 순으로 학생 순위 출력
    print("▷ 순위 : ")
    # 전체 학생을 점수 순으로 정렬
    rank = sorted(students.items(), key=lambda x: x[1], reverse=True)
    for i, (name, score) in enumerate(rank, 1):
        print(f"{i}위 : {name} ({score}점)")

# 실행
student_grade_manager()


'''2번 : https://100.pyalgo.co.kr/?page=5'''
def solution(data):
    # 리스트가 비어있으면 0 반환
    if len(data) == 0:
        return 0
    total_count = 0
    # 각 숫자에서 '1'의 개수를 세어서 합계
    for num in data:
        ones = str(num).count('1')
        total_count += ones
    return total_count
print(solution([1, 11, 111, 1111]))  # 10 (1+2+3+4)
print(solution([10, 21, 31, 101]))   # 5 (1+1+1+2)
print(solution([]))                  # 0