from rest_framework.serializers import ModelSerializer
from post.models import Post, Lang


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'text'
        ]

class LangDetailSerializer(ModelSerializer):
    class Meta:
        model = Lang
        fields = [
            'id',
            'title',
            'text',
            'data',
        ]
