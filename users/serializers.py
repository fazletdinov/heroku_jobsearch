from rest_framework import serializers
from .models import MyUser
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}

    def get_tokens(self, user):
        tokens = RefreshToken.for_user(user)

        return {
            'refresh': str(tokens),
            'access': str(tokens.access_token),
        }

    def create(self, validated_data):
        user = MyUser(email=self.validated_data['email'])
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user
