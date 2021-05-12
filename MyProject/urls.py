from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # this will map the path to api basic urls which will have all other endpoint links
    path('', include('api_basic.urls'))
]
