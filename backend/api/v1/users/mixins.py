from rest_framework.response import Response
from rest_framework.decorators import action


class UserActivityMixin:
    @action(detail=False, methods=['get'])
    def activity(self, request, *args, **kwargs):
        user = request.user
        data = {
            'last_login': user.last_login,
            'last_article': user.article_set.order_by('-created_at').first(),
            'likes_given': user.user_likes.count()
        }
        return Response(data)