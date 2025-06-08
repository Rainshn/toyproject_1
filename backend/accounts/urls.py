from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('signup_complete/', views.signup_complete_view, name='signup_complete'),
    path('signup_google/', views.signup_google_view, name='signup_google'),
    path('nickname/', views.nickname_view, name='nickname'),
    path('check-username/', views.check_username, name='check_username'),
    path('logout/', views.logout_view, name='logout'),
    path('withdrawal/', views.withdrawal_view, name='withdrawal'),
]
