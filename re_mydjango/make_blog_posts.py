import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from pyhub.llm import OpenAILLM, UpstageLLM
from django.conf import settings
from pydantic import BaseModel
from blog.models import Post

class BlogPost(BaseModel):
    title:str
    content:str

llm = OpenAILLM(
    api_key=settings.OPENAI_API_KEY,
    model="gpt-4o-mini",
    system_prompt="니는 맛집을 찾아다니는 미식가다. 유저가 제시하는 음식을 맛집 리스트로 가게이름과 메뉴를 정리해줘라",
    max_tokens=8000,
)

keywords = ["옥수수빵", "감자빵", "고구마빵",]

for keyword in keywords:
    reply = llm.ask(keyword, schema=BlogPost, use_history=False,)

    print(reply)
    blog_post: BlogPost = reply.structured_data

    post = Post()
    post.title = blog_post.title
    post.content = blog_post.content
    post.save()

    print("saved post #", post.id)