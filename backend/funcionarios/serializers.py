from rest_framework import serializers
from .models import Funcionario
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class FuncionarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Funcionario
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        # Cria o perfil do funcionário sem o usuário associado
        funcionario = Funcionario.objects.create(**validated_data)
        # Cria o usuário associado usando a chave como username
        user = User.objects.create_user(
            username=funcionario.chave,
            email=user_data.get('email'),
            password=user_data.get('password', 'SenhaPadrao!123')
        )
        funcionario.user = user
        funcionario.save()
        return funcionario

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.email = user_data.get('email', user.email)
            if 'password' in user_data:
                user.set_password(user_data['password'])
            user.save()
        return super().update(instance, validated_data)
