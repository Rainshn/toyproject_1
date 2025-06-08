from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("로그인 성공! 홈 페이지로 이동!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('main.urls', 'main'), namespace='main')),
    path('accounts/', include('accounts.urls')), # 무조건 accounts.urls이 allauth.urls 위에 위치해야 합니다!
    path('accounts/', include('allauth.urls')),  # django-allauth URL
    path('dreams/', include('dreams.urls')),
]
