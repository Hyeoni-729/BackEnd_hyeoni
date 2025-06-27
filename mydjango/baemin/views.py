from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

# 리스트 목록 구현을 위한 최소한의 ListView 클래스
shop_list = ListView.as_view(
    model=Shop,
    paginate_by=5,
    )


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