from rest_framework import serializers
from apps.articles.models import Article
from apps.users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователей

    :id: ID пользователя
    :email: Email пользователя
    """

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email'
        )

class ArticleSerializer(serializers.ModelSerializer):
    """
    Сериализатор текста

    :id: ID
    :email: Email
    :total_likes: количество лайков
    :total_dislikes: количество дизлайков
    :user_reactions: реакция пользователя (None если нет реакции)
    """
    owner = serializers.ReadOnlyField(source='owner.email')
    total_likes = serializers.IntegerField(read_only=True)
    total_dislike = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'total_likes',
            'total_dislike'
        ]
        read_only_fields = ('id',)