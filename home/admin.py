from django.contrib import admin

from .models import Authors , Article

# Register your models here.
admin.site.register(Authors)
admin.site.register(Article)