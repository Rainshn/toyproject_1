from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import DreamKeyword, DreamRecord

## 꿈 기록 화면
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def dream_write_view(request):
    # 감정 이모지
    feelings = [
        {'emoji': '😃', 'name': '행복'},
        {'emoji': '😊', 'name': '기쁨'},
        {'emoji': '😢', 'name': '슬픔'},
        {'emoji': '😠', 'name': '분노'},
        {'emoji': '😱', 'name': '공포'},
        {'emoji': '😬', 'name': '불안'},
        {'emoji': '🤔', 'name': '혼란'},
        {'emoji': '😵', 'name': '당황'},
    ]

    # 4x2 행렬로 나누기
    feelings_rows = [feelings[i:i+4] for i in range(0, len(feelings), 4)]

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

    return render(request, 'dreams/dream_write.html', {'feelings_rows': feelings_rows,})

## 꿈 기록 화면 (다음 버튼 누른 후)
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def dream_detail_view(request, dream_id):
    dream = get_object_or_404(DreamRecord, id=dream_id)
    return render(request, 'dreams/dream_detail.html', {'dream': dream})

# 로그인한 사용자의 꿈 기록만 가져오기
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def dream_list_view(request):
    dreams = DreamRecord.objects.filter(user=request.user).order_by('-id')  # 최신순 정렬
    return render(request, 'dreams/dream_list.html', {'dreams': dreams})

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