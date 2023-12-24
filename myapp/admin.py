from django.contrib import admin

# Register your models here.

from .models import movies_model

admin.site.register(movies_model)
