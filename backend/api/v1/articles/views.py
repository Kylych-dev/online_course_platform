from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from rest_framework import permissions, viewsets
from apps.articles.models import Article
from api.common.permissions import IsOwnerOrReadOnly

from api.v1.articles.serializers import ArticleSerializer
from .mixins import ReactionMixin


class ArticleViewSet(ReactionMixin, viewsets.ModelViewSet):
    """
    Methods:
        GET /article/ - список постов
        POST /article/ - создание поста
        GET /article/{id}/ - детали поста
        POST /article/{id}/like/ - лайк
        POST /article/{id}/dislike/ - дизлайк
        DELETE /article/{id}/unlike/ - удаление реакции
        GET /article/{id}/fans/ - список реакций
    """
    serializer_class = ArticleSerializer

    def get_permissions(self):
        if self.action in ['like', 'dislike', 'unlike', 'fans']:
            return [permissions.IsAuthenticated(), permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]

    def get_queryset(self):
        return Article.objects.annotate(
            total_likes=Count(
                'article_likes',
                filter=Q(article_likes__is_like=True),
                distinct=True
            ),
            total_dislike=Count(
                'article_likes',
                filter=Q(article_likes__is_like=False),
                distinct=True
            )
        ).select_related('owner').prefetch_related('article_likes')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print('Response data: ', response.data)
        return response



'''
Article.objects.all()
http://127.0.0.1:8000/api/v1/articles/
|------|-----------|----------|----------|----------|------------|
| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |    6     |    0     |    6     |     5      |
|------|-----------|----------|----------|----------|------------|

http://127.0.0.1:8000/api/v1/articles/
|------|-----------|----------|----------|----------|------------|
| Type | Database  |   Reads  |  Writes  |  Totals  | Duplicates |
|------|-----------|----------|----------|----------|------------|
| RESP |  default  |    3     |    0     |    3     |     0      |
|------|-----------|----------|----------|----------|------------|
Total queries: 3 in 0.0087s 
[21/Feb/2025 17:22:43] "GET /api/v1/articles/ HTTP/1.1" 200 242
'''

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