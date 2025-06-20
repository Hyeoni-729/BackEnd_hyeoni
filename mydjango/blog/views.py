from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from blog.models import Comment
from blog.forms import CommentForm

# 목록 조회
post_List = ListView.as_view(
    model=Post,
    # 생략하면 "앱이름/모델명소문자_list.html"을 자동으로 찾아준다
    # template_name="blog/post_list.html"
)

# 단건 조회
post_detail = DetailView.as_view(
    model=Post,
)

# 생성
Comment_new = CreateView.as_view(
    model=Comment,
    form_class=CommentForm,
    success_url="/blog/",
)