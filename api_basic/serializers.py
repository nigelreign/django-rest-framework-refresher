from rest_framework import serializers
from .models import Article

#serializers are used to convert instances into json like what a converter would do

# =====================================================================================================================
# using ModelSerializers
# =====================================================================================================================

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # to get specific fields
        # fields = [ 'id', 'title', 'author' ]

        # to get all fiels
        fields = '__all__'




# =====================================================================================================================
# using serializers
# =====================================================================================================================
# class ArticleSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=100, default="title")
    # author = serializers.CharField(max_length=100, default="author")
    # email = serializers.EmailField(max_length=100, default="email")
    # date = serializers.DateTimeField()

    # def create(self, validated_data):
    #     return Article.objects.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.date = validated_data.get('date', instance.date)
    #     instance.save()

    #     return instance
