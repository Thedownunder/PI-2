from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Funcionario
from .serializers import FuncionarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

class FuncionarioViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar ou editar funcionários.
    """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    View personalizada para login que verifica se o usuário precisa alterar a senha.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        username = request.data.get('username')
        user = User.objects.get(username=username)
        profile = user.funcionario

        # Verifica se a senha expirou
        if profile.password_expired():
            profile.must_change_password = True
            profile.save()

        if profile.must_change_password:
            return Response({
                "detail": "É necessário alterar a senha.",
                "must_change_password": True
            }, status=status.HTTP_403_FORBIDDEN)

        # Calcula os dias até a expiração
        days_left = profile.days_until_expiration()
        if days_left <= 7:
            response.data['password_expires_in'] = days_left
            response.data['warning'] = f"Sua senha expirará em {days_left} dias."

        return response

class ChangePasswordView(APIView):
    """
    Endpoint para que o usuário altere sua senha.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.funcionario
        senha_atual = request.data.get('senha_atual')
        nova_senha = request.data.get('nova_senha')

        if not user.check_password(senha_atual):
            return Response({"erro": "Senha atual incorreta."}, status=status.HTTP_400_BAD_REQUEST)

        if check_password(nova_senha, user.password):
            return Response({"erro": "A nova senha não pode ser igual à senha atual."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(nova_senha, user)
        except ValidationError as e:
            return Response({"erro": e.messages}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(nova_senha)
        user.save()
        profile.password_last_changed = timezone.now()
        profile.must_change_password = False
        profile.save()
        return Response({"sucesso": "Senha alterada com sucesso."}, status=status.HTTP_200_OK)
