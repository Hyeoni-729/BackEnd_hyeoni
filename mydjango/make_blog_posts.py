import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

from pyhub.llm import OpenAILLM, UpstageLLM
from django.conf import settings
from pydantic import BaseModel  # 추가
from blog.models import Post


class BlogPost(BaseModel):
    title: str
    content: str


llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    model="gpt-4o-mini",
    system_prompt="""니는 여행 블로거다. 유저가 제시하는 내용에 맞춰서 블로그의 제목과 내용 작성해줘""",
    max_tokens=8000,
)

# 키워드로 블로그 포스팅
keywords = ["부산 돼지국밥", "붕어빵",]

for keyword in keywords:
    reply = llm.ask(
        keyword,
        schema=BlogPost,
        use_history=False,
    )
    print(reply)
    blog_post: BlogPost = reply.structured_data

    post = Post()
    post.title = blog_post.title
    post.content = blog_post.content
    post.save()

    print("saved post #", post.id)
