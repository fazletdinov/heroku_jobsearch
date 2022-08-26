from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .models2 import *
from .serializers import *
from django.http import HttpResponse
from .permissions import IsAuthorOrReadOnly

def dashboard(request):
    return HttpResponse("<h1>Hello World</h1>")

class RegisterUserApiView(generics.CreateAPIView):
    queryset = MyUser.objects.using("default").all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserListApi(generics.ListAPIView):
    queryset = MyUser.objects.using('default').all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]

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