from django.contrib import admin
from contetnts.models import Content, Image

class ImageInline(admin.TabularInline):
    model = Image

class ContentAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Content, ContentAdmin)

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)

