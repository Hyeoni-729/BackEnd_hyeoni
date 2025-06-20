from django.views.generic import ListView, DetailView
from .models import Post

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

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, "blog/post_detail.html", {"post":post})