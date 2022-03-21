from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from API.serializers import *
from API.models import *


class ArticleListView_2(APIView):
    """Информация о статье"""
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)


class AuthorListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = Article.objects.all()
        params = self.request.query_params

        auth_id = params.get('author', None)

        if auth_id:
            queryset = queryset.filter(auth_id=auth_id)

        return queryset


class CategoryListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = Article.objects.all()
        params = self.request.query_params

        category_id = params.get('category', None)

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class TagListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = Article.objects.all()
        params = self.request.query_params

        tags_id = params.get('tag', None)

        if tags_id:
            queryset = queryset.filter(tags_id__id=tags_id)

        return queryset


class DateListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.all()

    def get_queryset(self):
        queryset = Article.objects.all()
        params = self.request.query_params

        date_of_pub = params.get('date', None)

        if date_of_pub:
            queryset = queryset.filter(date_of_pub=date_of_pub)

        return queryset