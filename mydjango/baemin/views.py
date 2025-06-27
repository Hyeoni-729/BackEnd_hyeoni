from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView


class ShopListView(ListView):
    model=Shop # 콤마 쓰면 리스트로 바뀌기 때문에 쓰면 안됨
    paginate_by=5
    # template_name="baemin/shop_list.html" # 디폴트 설정
    
    # 요청에 따라, 사용하는 템플릿을 변경해보자.
    # 부모 클래스의 get_template_names 메서드를 재정의 (오버라이드)
    def get_template_names(self):
        # 클래스 기반 뷰 현재 요청 객체 : self.request
        if "naked" in self.request.GET: # dict에서 해당 Key가 사전에 있는지만 확인
            # 무한 스크롤에서 다음 페이지 내용이라면?
            return "baemin/_shop_list.html"


        # 아래의 코드는 원래 메서드의 기본 동작을 수행
        return super().get_template_names()
    

# # 리스트 목록 구현을 위한 최소한의 ListView 클래스
# shop_list = ListView.as_view(
#     model=Shop,
#     paginate_by=5,
#     )

shop_list = ShopListView.as_view()


def shop_detail(request, pk):
    # shop = Shop.objects.get(pk=pk)
    shop = get_object_or_404(Shop, pk=pk)

    # 전체(모든 Shop) 리뷰 데이터를 가져올 준비.
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 (가져올 범위가 좁혀집니다.)
    review_qs = review_qs.filter(shop=shop)
    return render(
        request,
        template_name="baemin/shop_detail.html",
        context={"shop": shop, "review_list": review_qs},
    )

# @login_required : 로그인 상황이 아니면, 자동으로 로그인 페이지로 보낸다.
def review_new(request, shop_pk):
    # shop = Shop.objects.get(pk=shop_pk)
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "GET":
        form = ReviewForm()

    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_review = form.save(commit=False)
            unsaved_review.shop = shop
            unsaved_review.save()
            messages.success(request, "댓글이 성공적으로 등록되었습니다 🥰")
            shop_url = f"/baemin/{shop.pk}/"
            return redirect(shop_url)

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form, "shop": shop},
    )

def review_edit(request, shop_pk, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "GET":
        form = ReviewForm(instance=review)

    else:
        form = ReviewForm(instance=review, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "댓글이 성공적으로 수정되었습니다 😉")
            shop_url = f"/baemin/{shop_pk}/"
            return redirect(shop_url)

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form},
    )

def review_delete(request:HttpRequest, shop_pk:int, pk:int) -> HttpResponse:
    if request.method == "GET":
        return render(request, template_name="baemin/review_confirm_delete.html")
    
    review = get_object_or_404(Review, pk=pk) # 삭제할 리뷰 검색
    review.delete() # DB에서 호출 즉시 삭제

    messages.success(request, "댓글이 성공적으로 삭제되었습니다 😂")

    shop_url = f"/baemin/{shop_pk}/"
    return redirect(shop_url)