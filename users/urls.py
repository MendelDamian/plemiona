from django.urls import path
from .views import UserCreateView

app_name = "users"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="register"),
]
