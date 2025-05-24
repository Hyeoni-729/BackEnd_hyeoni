# 1. 총점, 평균 점수, '호준':98 추가 후 평균 점수, 모두 2점씩 추가, 가장 높고 낮은 학생의 이름과 점수를 구해라
student_score = {
    "홍의": 97,
    "원희": 60,
    "동해": 77,
    "변수": 79,
    "창현": 89,
}
## 총점, 평균 점수
score = sum(student_score.values())
avg = score / len(student_score)
print(f"총점 : {score} 평균 : {avg}")

## '호준':98 추가 후 평균 점수
student_score["호준"] = 98
avg2 = sum(student_score.values()) / len(student_score)
print(f"평균 : {avg2}")

## 모두 2점씩 추가
for name in student_score:
    student_score[name] += 2
for name, score in student_score.items():
    print(f"{name}:{score}점")

## 점수 가장 높은 학생의 이름과 점수
max_name = max(student_score, key=student_score.get)
max_score = student_score[max_name]
print(f"점수가 가장 높은 학생 : {max_name}|{max_score}점")

## 점수 가장 낮은 학생의 이름과 점수
min_name = min(student_score, key=student_score.get)
min_score = student_score[min_name]
print(f"점수가 가장 낮은 학생 : {min_name}|{min_score}점")


# 2. 학생들은 점심 메뉴를 고를 때, 한 명이라도 싫어하는 메뉴라면 고르지 않기로 했습니다. 최종 후보 메뉴들의 리스트를 구하는 코드를 작성해주세요.
like = ["볶음밥", "라면", "국수", "파스타", "치킨", "짜장면", "국밥"]
dislike = ["국밥", "짬뽕", "찜닭", "파스타", "국수", "카레", "덮밥"]
print(list(set(like) - set(dislike)))