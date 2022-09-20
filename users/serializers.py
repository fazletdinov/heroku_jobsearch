from rest_framework import serializers
from .models import MyUser, Resume, Vacancy, UserProfile
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


#class ProfileSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = UserProfile
#        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    resumes = serializers.HyperlinkedRelatedField(many=True, queryset=Resume.objects.all(),
                                                  view_name='resume-detail')
    vacansyes = serializers.HyperlinkedRelatedField(many=True, queryset=Vacancy.objects.all(),
                                                    view_name='vacansy-detail')

    class Meta:
        model = MyUser
        fields = ('url', 'id', 'email', 'resumes', 'vacansyes')

#    def update(self, instance, validated_data):
#        userprofile_serializer = self.fields['profile']
#        userprofile_instance = instance.userprofile
#        userprofile_data = validated_data.pop('userprofile', {})
#
#        userprofile_serializer.update(userprofile_instance, userprofile_data)
#        instance = super().update(instance, validated_data)
#        return instance

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'name', 'family', 'patronymic', 'date_of_birth', 'pol',
                  'country', 'city', 'emails', 'mobile', 'about_me', 'social', 'cv',
                  'portfolio', 'educational_institution', 'educational_institution_date',
                  'specialization', 'specialization_text', 'language', 'language_lvl_picmenno',
                  'language_lvl_yctno', 'hard_skills', 'soft_skills', 'user')

    def create(self, validated_data):
        profile = UserProfile.objects.create(user=self.context['request'].user, **validated_data)
        return profile

class ResumeSerializers(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(read_only=True, source='owner.email')
    class Meta:
        model = Resume
        fields = ('url', 'id', 'hard_skills', 'soft_skills', 'desired_position', 'desired_payment',
                  'photo', 'desired_place_of_work', 'about_me', 'checkbox', 'direction_of_activity',
                  'type_of_company', 'cv', 'resume', 'owner')

class VacansySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.CharField(read_only=True, source='owner.email')
    class Meta:
        model = Vacancy
        fields = ('url', 'id', 'company', 'looking_for_a_specialist', 'spialization', 'programming_language',
                  'type_of_activity', 'framework', 'soft_and_services', 'specialist_level', 'payment_amount',
                  'paymant', 'job_description', 'required_work_experience', 'type_of_work',
                  'location', 'location_bool', 'type_of_employment', 'working_draft', 'duration_of_work',
                  'hard_skills', 'soft_skills', 'language', 'language_picmen', 'language_yctno', 'quation1',
                  'quation2', 'quation3', 'health', 'food', 'working_conditions', 'education', 'finance_and_guarantees',
                  'entertainments', 'transport', 'job_manager', 'email', 'telephon', 'responses', 'receive_notifications',
                  'archive_it', 'when_to_publish', 'automatic_notification', 'additionally', 'owner')




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

