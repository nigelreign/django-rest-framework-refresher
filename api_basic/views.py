from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.
# View works as the accessor and the view as they are responsible for mapping the request and getting
# data from the db and pass it to the serializer


# ====================================================================================================================================
# Class Based API
# ====================================================================================================================================

# View set
# To bind these to the url you need to use routers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ModelView Set
# Well this one is the TRRRRRRRRRUUUUUUUUTTTTTHHHHH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# POST, GET, DELETE, PUT come shipped with this code
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    permission_classes = [IsAuthenticated]
    authentication_classes =  [JWTAuthentication]
    

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Generic View Set
# THIS IS THE BEST WAY DAMMMMMN!!!!!!!!!!!!!!!!!!!!!!
# it handles GET, POST, PUT and Delete in a few lines of code
# class ArticleViewSet(viewsets.GenericViewSet,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin):

#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# General View Set
# class ArticleViewSet(viewsets.ViewSet):

#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Generic api view
class GenericAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'

    # setting up session and basic authentication
    # Make sure its imported before using it
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    # authentication_classes = [TokenAuthentication]
    
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request):
        return self.destroy(request, id)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# General class
class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailsAPIView(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)

        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


# ====================================================================================================================================
# Funtion Based API
# ====================================================================================================================================
# @csrf_exempt is used to send POST request without sending csrf along with the POST data

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def article_list(request):
#     # this is responsible for all the GET requests coming to article
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         # return JsonResponse(serializer.data, safe = False)

#         # using restframework to pass response instead of Jsonresponse
#         return Response(serializer.data)

#     # this is responsible for all the POST requests
#     elif request.method == 'POST':
#         # jsonresponse
#         # data = JSONParser().parse(request)
#         # serializer = ArticleSerializer(data=data)

#         # using restframework response instead of Jsonresponse
#         # restframework response
#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#                 # JsonResponse
#             # return JsonResponse(serializer.data, status=201)

#                 # restframework response
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#             # JsonResponse
#         # return JsonResponse(serializer.errors, status=400)

#             # restframework response
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # all urls with id will be directed to this section eg article/3/
# # pk stands for primary key
# # @csrf_exempt

# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     # retrieve request
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)

#         return Response(serializer.data)

#     # Update request
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Delete request
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
