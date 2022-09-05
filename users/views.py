import jwt
from rest_framework.response import Response
from rest_framework import generics, viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import *
from .models2 import *
from .serializers import *
from .permissions import IsAuthorOrReadOnly
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

def dashboard(request):
    return HttpResponse("<h1>Hello World</h1>")

class RegisterUserApiView(generics.CreateAPIView):
    queryset = MyUser.objects.using("default").all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = MyUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        #token = user_data['access']
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl = 'https://' + current_site + relativeLink + '?token=' + str(token)
        email_body = 'Привет ' + user.email + ' перейдите по ссылке ниже, ' \
                                                 'чтобы подтвердить свой адрес электронной почты \n' + absurl

        data = {'email_body': email_body, 'to_email': user.email,
                'email_subject': 'Подтвердите свой адрес электронной почты'}

        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(APIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = MyUser.objects.get(id=payload['user_id'])
            if not user.is_verify:
                user.is_verify = True
                #user.is_active = True
                user.save()
            return Response({'email': 'Успешно активирован'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Срок действия активации истек'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Недопустимый токен'}, status=status.HTTP_400_BAD_REQUEST)

class ResumeViewSetApi(viewsets.ModelViewSet):
    queryset = Resume.objects.using('default').all()
    serializer_class = ResumeSerializers
    #permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserListApi(viewsets.ReadOnlyModelViewSet):
    queryset = MyUser.objects.using('default').all()
    serializer_class = UserListSerializer

# Вакансии

class AdListView(generics.ListCreateAPIView):
    queryset = Ad.objects.using('DB').all()
    serializer_class = AdSerializer

class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.using('DB').all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthorOrReadOnly]

class BaListView(generics.ListCreateAPIView):
    queryset = Ba.objects.using('DB').all()
    serializer_class = BaSerializer

class BaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ba.objects.using('DB').all()
    serializer_class = BaSerializer
    permission_classes = [IsAuthorOrReadOnly]

class BackendListView(generics.ListCreateAPIView):
    queryset = Backend.objects.using('DB').all()
    serializer_class = BackendSerializer

class BackendDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Backend.objects.using('DB').all()
    serializer_class = BackendSerializer
    permission_classes = [IsAuthorOrReadOnly]

class DesignerListView(generics.ListCreateAPIView):
    queryset = Designer.objects.using('DB').all()
    serializer_class = DesignerSerializer

class DesignerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designer.objects.using('DB').all()
    serializer_class = DesignerSerializer
    permission_classes = [IsAuthorOrReadOnly]

class DevopsListView(generics.ListCreateAPIView):
    queryset = Devops.objects.using('DB').all()
    serializer_class = DevopsSerializer

class DevopsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devops.objects.using('DB').all()
    serializer_class = DevopsSerializer
    permission_classes = [IsAuthorOrReadOnly]

class FrontendListView(generics.ListCreateAPIView):
    queryset = Frontend.objects.using('DB').all()
    serializer_class = FrontendSerializer

class FrontendDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Frontend.objects.using('DB').all()
    serializer_class = FrontendSerializer
    permission_classes = [IsAuthorOrReadOnly]

class FullstackListView(generics.ListCreateAPIView):
    queryset = Fullstack.objects.using('DB').all()
    serializer_class = FullstackSerializer

class FullstackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fullstack.objects.using('DB').all()
    serializer_class = FullstackSerializer
    permission_classes = [IsAuthorOrReadOnly]

class GameListView(generics.ListCreateAPIView):
    queryset = Game.objects.using('DB').all()
    serializer_class = GameSerializer

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.using('DB').all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthorOrReadOnly]

class HrListView(generics.ListCreateAPIView):
    queryset = Hr.objects.using('DB').all()
    serializer_class = HrSerializer

class HrDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hr.objects.using('DB').all()
    serializer_class = HrSerializer
    permission_classes = [IsAuthorOrReadOnly]

class MarketingListView(generics.ListCreateAPIView):
    queryset = Marketing.objects.using('DB').all()
    serializer_class = MarketingSerializer

class MarketingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marketing.objects.using('DB').all()
    serializer_class = MarketingSerializer
    permission_classes = [IsAuthorOrReadOnly]

class MobileListView(generics.ListCreateAPIView):
    queryset = Mobile.objects.using('DB').all()
    serializer_class = MobileSerializer

class MobileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.using('DB').all()
    serializer_class = MobileSerializer
    permission_classes = [IsAuthorOrReadOnly]

class NosortListView(generics.ListCreateAPIView):
    queryset = NoSort.objects.using('DB').all()
    serializer_class = NosortSerializer

class NosortDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoSort.objects.using('DB').all()
    serializer_class = NosortSerializer
    permission_classes = [IsAuthorOrReadOnly]

class PmListView(generics.ListCreateAPIView):
    queryset = Pm.objects.using('DB').all()
    serializer_class = PmSerializer

class PmDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pm.objects.using('DB').all()
    serializer_class = PmSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.using('DB').all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.using('DB').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthorOrReadOnly]

class QaListView(generics.ListCreateAPIView):
    queryset = Qa.objects.using('DB').all()
    serializer_class = QaSerializer

class QaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qa.objects.using('DB').all()
    serializer_class = QaSerializer
    permission_classes = [IsAuthorOrReadOnly]

class UsersListView(generics.ListCreateAPIView):
    queryset = Users.objects.using('DB').all()
    serializer_class = UsersSerializer

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.using('DB').all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthorOrReadOnly]

# на основе viewset

class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.using('DB').all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthorOrReadOnly]

class BaViewSet(viewsets.ModelViewSet):
    queryset = Ba.objects.using('DB').all()
    serializer_class = BaSerializer
    permission_classes = [IsAuthorOrReadOnly]

class BackendViewSet(viewsets.ModelViewSet):
    queryset = Backend.objects.using('DB').all()
    serializer_class = BackendSerializer
    permission_classes = [IsAuthorOrReadOnly]

class DesignerViewSet(viewsets.ModelViewSet):
    queryset = Designer.objects.using('DB').all()
    serializer_class = DesignerSerializer
    permission_classes = [IsAuthorOrReadOnly]

class DevopsViewSet(viewsets.ModelViewSet):
    queryset = Devops.objects.using('DB').all()
    serializer_class = DevopsSerializer
    permission_classes = [IsAuthorOrReadOnly]

class FrontendViewSet(viewsets.ModelViewSet):
    queryset = Frontend.objects.using('DB').all()
    serializer_class = FrontendSerializer
    permission_classes = [IsAuthorOrReadOnly]

class FullstackViewSet(viewsets.ModelViewSet):
    queryset = Fullstack.objects.using('DB').all()
    serializer_class = FullstackSerializer
    permission_classes = [IsAuthorOrReadOnly]

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.using('DB').all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthorOrReadOnly]

class HrViewSet(viewsets.ModelViewSet):
    queryset = Hr.objects.using('DB').all()
    serializer_class = HrSerializer
    permission_classes = [IsAuthorOrReadOnly]

class MarketingViewSet(viewsets.ModelViewSet):
    queryset = Marketing.objects.using('DB').all()
    serializer_class = MarketingSerializer
    permission_classes = [IsAuthorOrReadOnly]

class MobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.using('DB').all()
    serializer_class = MobileSerializer
    permission_classes = [IsAuthorOrReadOnly]

class NosortViewSet(viewsets.ModelViewSet):
    queryset = NoSort.objects.using('DB').all()
    serializer_class = NosortSerializer
    permission_classes = [IsAuthorOrReadOnly]

class PmViewSet(viewsets.ModelViewSet):
    queryset = Pm.objects.using('DB').all()
    serializer_class = PmSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.using('DB').all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthorOrReadOnly]

class QaViewSet(viewsets.ModelViewSet):
    queryset = Qa.objects.using('DB').all()
    serializer_class = QaSerializer
    permission_classes = [IsAuthorOrReadOnly]

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.using('DB').all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthorOrReadOnly]