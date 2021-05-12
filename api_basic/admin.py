from django.contrib import admin
from .models import Article

# Register your models here. so that you can be to access it as 
# http://127.0.0.1:8000/admin/api_basic/article/

admin.site.register(Article)
