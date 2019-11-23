from django.urls import path

from . import views

urlpatterns=[
    path('', views.Home.as_view(), name='home'),
    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]