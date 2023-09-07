#from django.conf.urls import url
#from django.conf.urls import url, include #instead of url
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
#from simplesocial.accounts import views
from . import views


app_name = "accounts",
app_name = "posts"



urlpatterns = [
    path('create/', views.render, name='create'), 
    path(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    path(r"signup/$", views.SignUp.as_view(), name="signup")
]