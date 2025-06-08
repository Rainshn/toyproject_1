from django.urls import path
from . import views

app_name = 'dreams'

urlpatterns = [
    #path('search/', views.search_keyword_view, name='search_keyword'),
    path('dream_write/', views.dream_write_view, name='dream_write'),
    path('dream_detail/<int:dream_id>/', views.dream_detail_view, name='dream_detail'),
    path('dream_list/', views.dream_list_view, name='dream_list'),
]