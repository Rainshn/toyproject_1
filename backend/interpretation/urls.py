from django.urls import path
from . import views

app_name = 'interpretation'
urlpatterns = [
    path('interpretation/<str:content>' , views.interpretation_view, name='interpretation'),
]