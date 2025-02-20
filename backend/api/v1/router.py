from django.urls import path
from rest_framework.routers import DefaultRouter
from api.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        path('register/', auth_views.RegisterView.as_view(), name='register'),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
)