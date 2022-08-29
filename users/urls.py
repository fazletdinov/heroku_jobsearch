from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()
router.register('ad', views.AdViewSet, basename='ad')
router.register('ba', views.BaViewSet, basename='ba')
router.register('backend', views.BackendViewSet, basename='backend')
router.register('designer', views.DesignerViewSet, basename='designer')
router.register('devops', views.DevopsViewSet, basename='devops')
router.register('frontend', views.FrontendViewSet, basename='frontend')
router.register('fullstack', views.FullstackViewSet, basename='fullstack')
router.register('game', views.GameViewSet, basename='game')
router.register('hr', views.HrViewSet, basename='hr')
router.register('marketing', views.MarketingViewSet, basename='marketing')
router.register('mobile', views.MobileViewSet, basename='mobile')
router.register('nosort', views.NosortViewSet, basename='nosort')
router.register('pm', views.PmViewSet, basename='pm')
router.register('product', views.ProductViewSet, basename='product')
router.register('qa', views.QaViewSet, basename='qa')
router.register('users', views.UsersViewSet, basename='users')

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('register/', views.RegisterUserApiView.as_view(), name='token_obtain_pair'),
    path('users-list/', views.UserListApi.as_view()),
    #path('api-auth/', include('rest_framework.urls')),
    #path('auth/', include('djoser.urls')),
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', include(router.urls)),
    path('account/', include('rest_email_auth.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)