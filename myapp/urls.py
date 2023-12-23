from django.urls import path
from . views import movie
from .views import template_view

urlpatterns=[
    path('movie', movie),
    path('temp', template_view)
]