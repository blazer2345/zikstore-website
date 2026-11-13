from django.urls import path
from . import views

urlpatterns=[
    path("homepage/", views.homepage, name="homepage"),
      path("record/", views.usersDeta, name="record"),
    path("signup/", views.signupForm, name="signup"),
    path("login/", views.loginForm, name="login"),
]