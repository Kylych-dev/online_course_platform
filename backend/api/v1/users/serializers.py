from rest_framework import serializers
from apps.users.models import CustomUser
from apps.articles.models import Article

class UserProfileSerializer(serializers.ModelSerializer):
    get_total_posts = serializers.IntegerField(read_only=True)
    get_total_likes = serializers.IntegerField(read_only=True)
    get_total_dislikes = serializers.IntegerField(read_only=True)


    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'get_total_likes',
            'get_total_dislikes',
            'get_total_posts'
        )


# class ArticleSerializer(serializers.ModelSerializer):
#     """
#     Сериализатор текста
#
#     :id: ID
#     :email: Email
#     :total_likes: количество лайков
#     :total_dislikes: количество дизлайков
#     :user_reactions: реакция пользователя (None если нет реакции)
#     """
#     owner = serializers.ReadOnlyField(source='owner.email')
#     total_likes = serializers.IntegerField(read_only=True)
#     total_dislike = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Article
#         fields = [
#             'id',
#             'owner',
#             'title',
#             'content',
#             'total_likes',
#             'total_dislike'
#         ]
#         read_only_fields = ('id',)