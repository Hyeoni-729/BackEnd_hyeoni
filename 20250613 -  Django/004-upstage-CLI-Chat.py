# 1) 라이브러리 설치 : openai
# 2) API KEY 미지정

from openai import OpenAI
'''
client = OpenAI("api키주소")

messages: list[dict] = [
    {
        "role": "system",  # system, user, assistant, function, ...
        "content": "닌 다양한 레시피를 알고 있는 조리사다",
    }
]  # 주의 : 끝에 콤마(,)가 있으면 안 된다.


# 무한 루프 (break를 만나면 종료)
while True:
    # strip() : 좌우 화이트 스페이스(공백, 개행, 탭 문자)를 모두 제거
    human_message = input("Human : ").strip()  # 유저로부터 1줄을 입력받아 반환
    if human_message:
        messages.append(
            {
                "role": "user",
                "content": human_message,
            }
        )

        # stream 여부에 따라, 반환값이 다르다
        completion = client.chat.completions.create(
            model="solar-pro2-preview",  # 7/15까지 무료
            messages=messages,
        )

        # assistant 메시지
        ai_message = completion.choices[0].message.content
        messages.append(
            {
                "role": "assistant",
                "content": human_message,
            }
        )
        print("AI :", ai_message)
'''