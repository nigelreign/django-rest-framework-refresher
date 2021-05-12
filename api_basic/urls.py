from django.urls import path, include
# from .views import article_list, article_detail, ArticleAPIView
from .views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# register the router
router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

# this is where we will map our endpoints
# we get article_list from views in the same directory we are in
urlpatterns = [
    # redirecting to function based
    # path('article/', article_list),
    # path('article/<int:pk>/', article_detail),

    # redirecting to class based
    path('generic/<int:id>/', GenericAPIView.as_view()),
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetailsAPIView.as_view()),

    # viewset
    path('api/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # JWT auth URL
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
