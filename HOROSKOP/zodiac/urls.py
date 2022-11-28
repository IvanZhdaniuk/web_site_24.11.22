
from django.urls import path
from zodiac import views

urlpatterns = [
    path('', views.home_page, name='zodiac-home'),
    path('<str:sign_name>/', views.zod, name='zod-ditail'),
    path('<str:sign_name>/', views.get_sign, name='zodiac-sign'),



]
