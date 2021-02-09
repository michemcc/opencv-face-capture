from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'capture'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('detect/', views.detect, name='detect'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)