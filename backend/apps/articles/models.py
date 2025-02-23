from django.db import models
from apps.users.models import CustomUser


class Article(models.Model):

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_likes')
    is_like = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            'user',
            'article'
        )


