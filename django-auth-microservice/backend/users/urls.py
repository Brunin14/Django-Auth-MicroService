from django.urls import path
from .register import EmailRegisterView
from .jwt_login import JWTLoginView
from .jwt_refresh import JWTRefreshView
from .jwt_logout import JWTLogoutView
from .me import MeView

app_name = "users"

urlpatterns = [
    path("registration/", EmailRegisterView.as_view(), name="custom_register"),

    path("login/", JWTLoginView.as_view(), name="jwt_login"),

    path("token/refresh/", JWTRefreshView.as_view(), name="jwt_refresh"),

    path("me/", MeView.as_view(), name="me"),

    path("logout/", JWTLogoutView.as_view(), name="jwt_logout"),


]



