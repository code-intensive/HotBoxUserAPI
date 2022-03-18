from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, ViewUsers

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('user', UserView.as_view(), name="user"),
    path('users', ViewUsers.as_view(), name="users"),
    path('logout', LogoutView.as_view(), name="logout"),
]
