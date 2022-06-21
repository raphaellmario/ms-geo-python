from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('tecban.urls', namespace='tecban')),
    path('admin/', admin.site.urls),
]
