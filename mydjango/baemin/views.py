from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop, Review
from .forms import ReviewForm
from django.http import HttpRequest, HttpResponse


def shop_list(request):
    # DB에서 baemin_shop 테이블의 모든 레코드를 조회할 준비
    qs = Shop.objects.all()
    # qs = qs.order_by('-id') # 매번 정렬을 이렇게 지정해줄수 있지만, DB입장에서는 매우 부담
    # qs = qs[0:5] # 처음 5개 (리스트/문자열의 슬라이싱 문법과 동일)
    # qs = qs[5:10] # 2페이지
    # qs = qs[10:15] # 3페이지

    page = 1
    paginate_by = 5 # 1페이지를 몇 개씩 끊는지 설정

    start_index = (page - 1) * paginate_by
    end_index = page * paginate_by
    qs = qs[start_index:end_index]

    return render(
        request,
        template_name="baemin/shop_list.html",
        context={
            "shop_list": qs,
        },
    )


def shop_detail(request, pk):
    # shop = Shop.objects.get(pk=pk)
    shop = get_object_or_404(Shop, pk=pk)

    # 전체(모든 Shop) 리뷰 데이터를 가져올 준비.
    review_qs = Review.objects.all()
    # 특정 shop의 리뷰 데이터를 가져올 준비 (가져올 범위가 좁혀집니다.)
    review_qs = review_qs.filter(shop=shop)

    # 정렬을 지정하지 않아도 출력은 된다.
    # 저장된 순서대로 조회된다. 조회할 때마다 다른 순서로 조회가 된다.
    # review_qs = review_qs.order_by("id") # id 필드 오름차순
    # review_qs = review_qs.order_by("-id") # id 필드 내림차순(역순)


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

    # # 지정 조건의 레코드가 DB에 없을 때 Review.DoesNotExit 오류 발생
    # try:
    #     review = Review.objects.get(pk=pk) # 지정 조건의 레코드는 DB가 1개 존재.
    # except Review.DoesNotExist:
    #     raise Http404

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