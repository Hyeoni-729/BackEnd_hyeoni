# 1) 라이브러리 설치 : openai
# 2) API KEY 미지정

from openai import OpenAI
'''
client = OpenAI("api키주소")


# stream 여부에 따라, 반환값이 다르다
stream = client.chat.completions.create(
    # model="solar-mini",
    model="solar-pro2-preview", # 7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "recipe",
        }
    ],
    stream=True, # ADDED
)

# stream=False : 통응답을 받을 때
# print(completion.choices[0].message.content)

# API 서버에서 내려준 chunk의 개수만큼 반복된다
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        # end 키워드 인자의 디폴트 값 : 개행("\n") = 줄바꿈
        print(chunk.choices[0].delta.content, end="")
'''