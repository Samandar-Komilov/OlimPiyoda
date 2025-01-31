from django.urls import path

from apps.users.api_endpoints import Login, Profile, Register, RegisterConfirm

urlpatterns = [
    path("register/", Register.RegisterAPIView.as_view(), name="register"),
    path(
        "register/confirm/<str:token>/", RegisterConfirm.RegisterConfirmAPIView.as_view(), name="register-confirmation"
    ),
    path("login/", Login.LoginAPIView.as_view(), name="login"),
    path("profile/", Profile.ProfileAPIView.as_view(), name="profile"),
]
