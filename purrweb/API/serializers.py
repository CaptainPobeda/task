from rest_framework import serializers
from API.models import *


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname')


class ArticleListSerializer(serializers.ModelSerializer):
    category_id = serializers.SlugRelatedField(slug_field="name", read_only=True)
    auth_id = AuthorListSerializer(read_only=True)
    tags_id = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleALLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
