from django.db.models import Count, Sum

from apps.articles.models import Article
from api.v1.articles.serializers import ArticleSerializer

def get_owner_stats(user):
    most_popular_article = user.article_set \
        .annotate(likes=Count('article_likes')) \
        .order_by('-likes') \
        .first()


    return {
        'articles': user.article_set.count(),
        'likes_received': Article.objects.filter(owner=user)
            .annotate(total=Count('article_likes'))
            .aggregate(total=Sum('total'))['total'],
        'most_popular_article': ArticleSerializer(most_popular_article).data if most_popular_article else None,


        # user.article_set
        #     .annotate(likes=Count('article_likes'))
        #     .order_by('-likes').first()
    }
