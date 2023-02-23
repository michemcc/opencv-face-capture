from django.contrib import admin
from .models import ImageUploadModel

class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('description', 'document', )

admin.site.register(ImageUploadModel, ImageUploadAdmin)