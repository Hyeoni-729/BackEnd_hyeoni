# 1) 라이브러리 설치 : openai
# 2) API KEY 미지정

from openai import OpenAI
'''
client = OpenAI("api키주소")

completion = client.chat.completions.create(
    # model="solar-mini",
    model="solar-pro2-preview", # 7/15까지 무료
    messages=[
        {
            "role": "user",
            "content": "hello",
        }
    ]
)

print(completion.choices[0].message.content)
'''