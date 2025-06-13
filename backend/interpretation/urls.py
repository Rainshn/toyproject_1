from django.urls import path
from . import views

app_name = 'interpretation'
urlpatterns = [
    path('interpretation/<str:content>' , views.interpretation_view, name='interpretation'),
    #저장 결과화면
    path('interp_save/<int:interpret_id>/', views.interpretation_save, name='interp_save'),
]