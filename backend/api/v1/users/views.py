from rest_framework import permissions, generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.articles.models import Article
from .serializers import UserProfileSerializer
from .mixins import UserActivityMixin
from .services import get_owner_stats
from api.v1.articles.serializers import ArticleSerializer

from api.common.permissions import IsProfileOwner


class ProfileView(UserActivityMixin, viewsets.GenericViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsProfileOwner]

    def get_object(self):
        return self.request.user

    @action(detail=True, methods=['get'])
    def stats(self, request):
        print('-=-=-=-=-=-==-=-')
        user = self.get_object()
        stats_data = get_owner_stats(user)
        return Response(stats_data)

    @action(detail=True, methods=['get'])
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ProfileActiveView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsProfileOwner]

    def get_queryset(self):
        return Article.objects.filter(owner=self.request.user)

