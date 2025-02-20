from django.db.models.aggregates import Count
from rest_framework import permissions, viewsets
from apps.articles.models import Article
from api.common.permissions import IsOwnerOrReadOnly

from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().prefetch_related('likes')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset().select_related('owner').prefetch_related('likes')
        # print(queryset, 'Article Queried -=-=-=-=')
        queryset = queryset.prefetch_related('likes')
        print(queryset.query)

        return queryset

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
| RESP |  default  |    5     |    0     |    5     |     3      |
|------|-----------|----------|----------|----------|------------|
Total queries: 5 in 0.0234s 





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