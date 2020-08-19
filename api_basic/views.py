from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    #List all Article or create a new article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer



class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    #Retreive, update, delete an article
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer




