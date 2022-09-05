from rest_framework import serializers
from .models import MyUser, Resume
from .models2 import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserRegistrationSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'tokens')
        extra_kwargs = {'password': {'write_only': True}}

#    def create(self, validated_data):
#        return MyUser.objects.create_user(**validated_data)

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
        user.save(using='default')
        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class BaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ba
        fields = '__all__'

class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backend
        fields = "__all__"

class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = "__all__"

class DevopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devops
        fields = "__all__"

class FrontendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frontend
        fields = "__all__"

class FullstackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullstack
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class HrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hr
        fields = "__all__"

class MarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        fields = "__all__"

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = "__all__"

class NosortSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoSort
        fields = "__all__"

class PmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pm
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class QaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qa
        fields = "__all__"

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class ResumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'