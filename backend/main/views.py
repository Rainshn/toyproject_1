from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from dreams.models import DreamKeyword

from dreams.models import DreamRecord


## 홈 화면
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def home_view(request):
    keywords = DreamKeyword.objects.filter(user=request.user).order_by('?')[:5]
    return render(request, 'main/home.html')

## 마이페이지
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def mypage_view(request):
    return render(request, 'main/mypage.html')

# 로그인한 사용자의 꿈 기록만 가져오기
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def saved_list_view(request):
    dreams = DreamRecord.objects.filter(user=request.user).order_by('-id')  # 최신순 정렬
    return render(request, 'main/saved_list.html', {'dreams': dreams})
