from django.urls import path
from . import views

urlpatterns = [
    path('register', views.lgn, name="register"),
    path('login_page', views.login_page, name="login_page"),
    path('logout', views.logout, name="logout")
]
