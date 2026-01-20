from dj_rest_auth.registration.views import RegisterView
from .serializers import EmailRegisterSerializer


class EmailRegisterView(RegisterView):
    serializer_class = EmailRegisterSerializer
