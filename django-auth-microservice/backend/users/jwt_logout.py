from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

# Novos Imports
from drf_spectacular.utils import extend_schema
from .serializers import LogoutSerializer

class JWTLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LogoutSerializer,
        summary="Logout (Blacklist Refresh Token)",
        description="Envia o Refresh Token para a lista negra. Requer autenticação com Access Token."
    )
    def post(self, request):
        refresh = request.data.get("refresh")
        
        # O resto do seu código continua igual...
        if not refresh:
            return Response({"detail": "refresh is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({"detail": "Logged out"}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"detail": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)