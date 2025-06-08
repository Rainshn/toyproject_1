from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('mypage/', views.mypage_view, name='mypage'),
]
