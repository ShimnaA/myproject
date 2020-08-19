from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class ArticleList(APIView):
    #List all Article or create a new article
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    #Retreive, update, delete an article
        def get_object(self, pk):
            try:
                return Article.objects.get(pk=pk)
            except Article.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            article = self.get_object(pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            article = self.get_object(pk)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            article =  self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

