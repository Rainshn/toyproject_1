# 구글 로그인 연동을 위한 어댑터입니다
# settings.py에 어댑터 설정 추가 필요!

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import resolve_url


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)
        if not user.nickname:
            user.nickname = 'temp'  # 임시 닉네임
            user.save()
        return user

    def get_login_redirect_url(self, request):
        user = request.user
        if user.is_authenticated:
            if not getattr(user, 'marketing_agreed', False):
                return resolve_url('signup_google')
            else:
                return resolve_url('main:home')
        return super().get_login_redirect_url(request)

