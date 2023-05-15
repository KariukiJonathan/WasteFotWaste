from django.urls import path
from django.contrib.auth.views import LoginView 
from .views import SignupView, main_page

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/',  SignupView, name='signup'),
    path('',  main_page, name='main-page'),
]
