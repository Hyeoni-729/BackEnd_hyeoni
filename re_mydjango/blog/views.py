from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from blog.models import Comment
from blog.forms import CommentForm

post_List = ListView.as_view(
    model=Post,
)

post_detail = DetailView.as_view(
    model=Post,
)

Comment_new = CreateView.as_view(
    model=Comment,
    form_class=CommentForm,
    success_url="/blog/",
)