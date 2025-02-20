from rest_framework import serializers
from apps.articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Article
        fields = [
            'id',
            'owner',
            'title',
            'content'
        ]
        read_only_fields = ('id',)

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