from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from api.auth import views as auth_views
from .articles import views as articles_views
from .users import views as users_views

router = DefaultRouter(trailing_slash=False)

urlpatterns = router.urls

urlpatterns.extend(
    [
        path('register/', auth_views.RegisterView.as_view(), name='register'),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

        path('articles/', articles_views.ArticleViewSet.as_view(
            {
                'get': 'list',
                'post': 'create'
            }
        ), name='articles'),
        path('articles/<int:pk>/', articles_views.ArticleViewSet.as_view(
            {
                'put': 'update',
                'get': 'retrieve',
            }
        ), name='article'),
        # path('profile/', users_views.ProfileView.as_view(), name='user-profile'),
        path('profile/activity/', users_views.ProfileView.as_view({'get':'retrieve'}), name='user-profile-activity'),
        path('profile/stats/', users_views.ProfileView.as_view({'get':'stats'}), name='user-profile-stats'),



        path('articles/<int:pk>/like/', articles_views.ArticleViewSet.as_view(
            {
                'post':'like',
            }
        ), name='article-like'),
        path('articles/<int:pk>/dislike/', articles_views.ArticleViewSet.as_view(
            {
                'post':'dislike',
            }
            ), name='article-dislike'),
    ]
)