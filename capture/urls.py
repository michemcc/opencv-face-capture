from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'capture'

urlpatterns = [
    path('', views.first_view, name='first_view'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('detect_face/', views.detect_face, name='detect_face'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)