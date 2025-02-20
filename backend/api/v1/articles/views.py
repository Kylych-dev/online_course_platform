from rest_framework import permissions, viewsets
from apps.articles.models import Article
from api.common.permissions import IsOwnerOrReadOnly

from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


    # def get_queryset(self):
    #     print(self.request.user, 'it is user')
    #     print(self.action, 'it is action')
    #
    #     return self.queryset.filter(owner=self.request.user)

    # @action(detail=True, methods=['get'])
    # def articles(self, request, pk=None):
    #     article = self.get_object()
    #     serializer = self.get_serializer(article, many=True)
    #     return Response(serializer.data)