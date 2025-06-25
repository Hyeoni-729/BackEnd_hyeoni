from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm
from django.contrib import messages


def shop_list(request):
    # DB에서 baemin_shop 테이블의 모든 레코드를 조회할 준비
    qs = Shop.objects.all()

    return render(
        request,
        template_name="baemin/shop_list.html",
        context={
            "shop_list": qs,
        },
    )


def shop_detail(request, pk):
    shop = Shop.objects.get(pk=pk)

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
    shop = Shop.objects.get(pk=shop_pk)

    if request.method == "GET":
        form = ReviewForm()

    else:
        form = ReviewForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_review = form.save(commit=False)
            unsaved_review.shop = shop
            unsaved_review.save()
            messages.success(request, "댓글이 성공적으로 등록되었습니다!")
            shop_url = f"/baemin/{shop.pk}/"
            return redirect(shop_url)

    return render(
        request,
        template_name="baemin/review_form.html",
        context={"form": form, "shop": shop},
    )
