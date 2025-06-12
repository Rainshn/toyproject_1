from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import DreamKeyword, DreamRecord

## 꿈 기록 화면
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def dream_write_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        context = request.POST.get('context')
        tags = request.POST.get('tags')
        feelings = request.POST.getlist('feelings')

        dream = DreamRecord.objects.create(
            user = request.user,
            title = title,
            context = context,
            tags = tags,
            feelings=", ".join(feelings), # 쉼표로 이어 붙여 저장
        )

        # 저장 후 상세 페이지로 이동
        return redirect('dreams:dream_detail', dream_id=dream.id)

    return render(request, 'dreams/dream_write.html')

@login_required
@csrf_exempt
@require_POST
def dream_create_api(request):
    title = request.POST.get('title')
    context = request.POST.get('context')
    tags = request.POST.get('tags')
    feelings = request.POST.getlist('feelings')

    dream = DreamRecord.objects.create(
        user=request.user,
        title=title,
        context=context,
        tags=tags,
        feelings=", ".join(feelings),
    )

    return JsonResponse({'dream_id': dream.id})


## 꿈 기록 화면 (다음 버튼 누른 후)
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def dream_detail_view(request, dream_id):
    dream = get_object_or_404(DreamRecord, id=dream_id)
    return render(request, 'dreams/dream_detail.html', {'dream': dream})

## 꿈 결과 화면 (해몽 보러가기 버튼 누른 후)
def dream_results_view(request):
    return render(request, 'dreams/dream_results.html')

# ## 키워드 검색 창
# def search_keyword(request):
#     query = request.GET.get('q', '' ) # 검색어 받아오고, 없으면 빈 문자열
#     results = []
#
#     if query:
#         results = DreamKeyword.objects.filter(keyword__icontains=query)
#
#     context = {
#         'query': query,
#         'results': results,
#     }
#     return render(request, 'main/search_results.html', context)