
from django.urls import path
from zodiac import views

urlpatterns = [
    path('', views.home_page, name='zodiac-home'),
    path('zod/', views.zod),

    path('<str:sign_name>/', views.get_sign, name='zodiac-sign'),
    path('about/', views.about, name='zodiac-about'),
    path('', views.zod),
    path('homepage/', views.home_page, name='zodiac-home-page'),

]
