# users/jwt_login.py
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import LoginBurstRateThrottle

# NOVOS IMPORTS
from drf_spectacular.utils import extend_schema
from .serializers import LoginSerializer

class JWTLoginView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [AnonRateThrottle, UserRateThrottle, LoginBurstRateThrottle]

    # ADICIONE ESTE DECORATOR EM CIMA DO POST
    @extend_schema(
        request=LoginSerializer,
        responses={200: LoginSerializer}, # Apenas documentação
        summary="Login via Email e Senha"
    )
    def post(self, request):
        # Aqui o código continua igual ao que você já tinha...
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"detail": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(request, username=email, password=password)

        if not user:
            return Response(
                {"detail": "Invalid credentials."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        refresh = RefreshToken.for_user(user)
        return Response(
            {"access": str(refresh.access_token), "refresh": str(refresh)},
            status=status.HTTP_200_OK,
        )