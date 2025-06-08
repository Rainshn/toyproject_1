from os.path import exists

from allauth.socialaccount.models import SocialAccount
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Post
from .forms import SignUpForm
from dreams.models import DreamKeyword, DreamRecord

User = get_user_model()

## 일반 회원가입
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # 필수 약관 동의 체크 여부 가져오기
        terms = request.POST.get('terms')
        privacy = request.POST.get('privacy')
        age = request.POST.get('age')

        # 필수 항목 체크 안 되었을 경우 에러 처리
        if not (terms and privacy and age):
            return render(request, 'accounts/signup.html', {
                'form': form,
                'error': '필수 약관에 모두 동의해주세요.'
            })

        if form.is_valid():
            user = form.save(commit=False)

            # 선택 약관 처리
            marketing = request.POST.get('marketing') == 'on'
            user.marketing_agreed = marketing
            user.save()

            # 회원가입 후 인증(backend 정보 포함)
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('/accounts/signup_complete/')

        # 유효성 검사 실패 시
        context ={
            'form': form,
            'username_error': form.errors.get('username'),
            'password1_error': form.errors.get('password1'),
            'password2_error': form.errors.get('password2'),
        }
        return render(request, 'accounts/signup.html', context)

    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

## 로그인
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # 로그인 성공 → 홈 페이지
        else:
            return render(request, 'accounts/login.html', {'error': '자격 증명 실패'})
    return render(request, 'accounts/login.html')

## 닉네임 설정
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def nickname_view(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        if nickname:
            request.user.nickname = nickname
            request.user.save()
            return redirect('/')  # 서비스 메인 페이지로 이동
    return render(request, 'accounts/nickname.html')

## Username 중복 확인
def check_username(request):
    username = request.GET.get('username')
    if not username:
        return JsonResponse({'valid': False, 'message': '아이디를 입력해주세요.'})
    username_exists = User.objects.filter(username=username).exists()
    if username_exists:
        return JsonResponse({'valid': False, 'message': '이미 사용 중인 아이디입니다.'})
    return JsonResponse({'valid': True, 'message': '사용 가능한 아이디입니다.'})

## 가입 완료
def signup_complete_view(request):
    return render(request, 'accounts/signup_complete.html')

## 구글 회원가입
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def signup_google_view(request):
    if not request.user.is_authenticated:
        # 로그인 안 되어 있으면 로그인 페이지로 리다이렉트
        return redirect('login')

    if request.method == 'POST':
        # 약관 체크
        terms = request.POST.get('terms')
        privacy = request.POST.get('privacy')
        age = request.POST.get('age')
        if not (terms and privacy and age):
            return render(request, 'accounts/signup_google.html', {
                'email': request.user.email,
                'error': '필수 약관에 모두 동의해주세요.'
            })

        # 마케팅 동의 여부 저장
        marketing = request.POST.get('marketing') == 'on'
        request.user.marketing_agreed = marketing
        request.user.save()

        # backend 지정
        request.user.backend = 'allauth.account.auth_backends.AuthenticationBackend'

        # 로그인 처리
        login(request, request.user)

        return redirect('/accounts/signup_complete/')  # 다음 단계로 이동

    else:
        return render(request, 'accounts/signup_google.html', {
            'email': request.user.email,
        })

## 로그아웃
@require_POST
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def logout_view(request):
    logout(request)
    return redirect('login')

## 회원 탈퇴
@require_POST
@login_required
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def withdrawal_view(request):
    user = request.user

    DreamKeyword.objects.filter(user=user).delete()
    DreamRecord.objects.filter(user=user).delete()

    logout(request) # 세션 로그아웃
    user.delete() # 유저 삭제
    return redirect('login')