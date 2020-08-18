from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        #Create and return a new article given the validated data
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        #Update and return an existing Article instance given the validated data
        instance.title = validated_data.get('title', instance.title)
        instance.author =  validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)