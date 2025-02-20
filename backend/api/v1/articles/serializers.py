from rest_framework import serializers
from apps.articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            'id',
            'owner',
            'title',
            'content',
            'likes'
        ]
        read_only_fields = ('id',)

    def get_likes(self, obj):
        # Возвращаем только количество лайков (или список id пользователей)
        return obj.likes.count() # Или obj.likes.values_list('id', flat=True)
'''


    {
        "id": 1,
        "owner": "user@mail.ru",
        "title": "qewrty tom form",
        "content": "This content is edited"
    },
    {
        "id": 2,
        "owner": "user2@mail.ru",
        "title": "edvard vachovski",
        "content": "hello dear subscriber my name is edvard vachoswky"
    }
    
    {
        "id": 1,
        "owner": "user@mail.ru",
        "title": "qewrty tom form",
        "content": "This content is edited"
    },
    {
        "id": 2,
        "owner": "user2@mail.ru",
        "title": "Edvard Vachovski",
        "content": "hello dear subscriber my name is edvard vachoswky"
    }

'''