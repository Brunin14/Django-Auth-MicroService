from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    # Suas rotas custom (JWT + register + me + logout + refresh)
    path("api/auth/", include("users.urls")),

    # Só rotas auxiliares do dj-rest-auth (sem login/logout/register)
    path("api/auth/", include("dj_rest_auth.urls")),  # password change/reset endpoints etc.
    # REMOVA a linha abaixo se seu register já é custom:
    # path("api/auth/registration/", include("dj_rest_auth.registration.urls")),

    # allauth (confirm email via link e social login flow)
    path("accounts/", include("allauth.urls")),
]
