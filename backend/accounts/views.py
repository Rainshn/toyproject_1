import json

from os.path import exists

from allauth.socialaccount.models import SocialAccount
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import SignUpForm
from dreams.models import DreamKeyword, DreamRecord

User = get_user_model()

## 일반 회원가입 - 0610 FE-BE 연결 테스트 위해 코드 수정
@csrf_exempt  # 개발 중에만 사용하세요
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': '유효하지 않은 JSON'}, status=400)

        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')
        terms = data.get('terms')
        privacy = data.get('privacy')
        age = data.get('age')
        marketing = data.get('marketing', False)

        if not (terms and privacy and age):
            return JsonResponse({'error': '필수 약관에 모두 동의해주세요.'}, status=400)

        form = SignUpForm({
            'username': username,
            'password1': password1,
            'password2': password2,
        })

        if form.is_valid():
            user = form.save(commit=False)
            user.marketing_agreed = marketing
            user.save()

            user = authenticate(request, username=username, password=password1)
            if user is not None:
                login(request, user)
                return JsonResponse({'message': '회원가입 완료'}, status=201)

            return JsonResponse({'error': '로그인 실패'}, status=400)

        return JsonResponse({'form_errors': form.errors}, status=400)

    else:
        return JsonResponse({'error': 'POST 요청만 허용됩니다'}, status=405)

## GET 전용
def signup_form_view(request):
    return render(request, 'accounts/signup.html')

## 로그인
@csrf_exempt # Postman 테스트용 CSRF 우회 - 개발 단계에서만 사용!!
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
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
        try:
            data = json.loads(request.body)
            nickname = data.get('nickname')
        except (json.JSONDecodeError, AttributeError):
            return JsonResponse({'error': '유효하지 않은 요청입니다.'}, status=400)

        if not nickname:
            return JsonResponse({'error': '닉네임을 입력해주세요.'}, status=400)

        user = request.user
        if not user.is_authenticated:
            return JsonResponse({'error': '로그인이 필요합니다.'}, status=401)

        user.nickname = nickname
        user.save()
        return JsonResponse({'message': '닉네임 설정 완료'}, status=200)

    # GET 요청일 때 닉네임 설정 폼 페이지 렌더링
    elif request.method == 'GET':
        return render(request, 'accounts/nickname.html')

    else:
        return JsonResponse({'error': '지원하지 않는 요청입니다.'}, status=405)

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

    # # User 테이블에 해당 이메일이 이미 존재하는지 확인
    # if User.objects.filter(email=email).exists():
    #     # 이미 존재하는 이메일이라면 중복 가입 방지
    #     return render(request, 'accounts/signup_google.html', {
    #         'email': request.user.email,
    #         'error': '이미 가입된 구글 계정 또는 이메일입니다.'
    #     })

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

## 가입 완료
def signup_google(request):
    return render(request, 'accounts/signup_google.html')


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