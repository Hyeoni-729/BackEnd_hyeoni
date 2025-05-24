# 중첩 반복문
movie = {
  '영화': '레미제라블',
  '장르': '드라마',
  '서비스': '디즈니',
  '비용': 15000,
  '평점': 4.9
}

if movie['장르'] == '드라마':
  if movie['서비스'] == '디즈니' or movie['서비스'] == '넷플릭스':
    if movie['평점'] >= 4.5:
      if movie['비용'] <= 20000:
        print('영화시청')


# match : 여러 조건을 체크하여 해당 조건에 맞는 코드 블록을 실행하는 제어문
text = 'hello world'
match text:
  case 'hello':
    print('hello')
  case 'world':
    print('world')
  case _:
    print('No Match') # No Match 출력