from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        u = request.user
        return Response({
            "id": u.id,
            "email": u.email,
            "is_active": u.is_active,
            "is_staff": u.is_staff,
            "last_login": u.last_login,
            "date_joined": u.date_joined,
        })
