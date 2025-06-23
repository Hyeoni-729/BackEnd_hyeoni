from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from blog.models import Comment
from blog.forms import CommentForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

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
# Comment_new = CreateView.as_view(
#     model=Comment,
#     form_class=CommentForm,
#     success_url="/blog/",
# )

# 함수 기반 뷰로 구현 해보기 (생성)
def comment_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    if request.method == "GET":
        form = CommentForm()
        
    else:  # POST
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.cleaned_data 

            unsaved_comment: Comment = form.save(commit=False)

            unsaved_comment.post = Post.objects.get(id=post_pk)
            unsaved_comment.save()


            post_url = f"/blog/{post_pk}/"
            return redirect(post_url)

    return render(request, "blog/comment_form.html", {
        "form" : form,
    })