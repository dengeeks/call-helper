from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularYAMLAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('schema/', SpectacularYAMLAPIView.as_view(), name='schema'),

]
