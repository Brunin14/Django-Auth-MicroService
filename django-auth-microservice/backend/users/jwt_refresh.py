from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

# --- NOVOS IMPORTS ---
from drf_spectacular.utils import extend_schema
from .serializers import RefreshTokenSerializer

class JWTRefreshView(APIView):
    permission_classes = [AllowAny]

    # --- ADICIONE ISTO AQUI EM CIMA DO POST ---
    @extend_schema(
        request=RefreshTokenSerializer,
        summary="Renovar Token de Acesso",
        description="Recebe um Refresh Token válido e retorna um novo Access Token."
    )
    def post(self, request):
        refresh = request.data.get("refresh")
        if not refresh:
            return Response({"detail": "refresh is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh)
            # O retorno padrão é só o access, conforme seu código original
            return Response({"access": str(token.access_token)}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)