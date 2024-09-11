
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #define um caminho, e direciona para a pasta api_rest.uls
    path('api/', include('api_rest.urls'), name='api_rest_urls'),
]
