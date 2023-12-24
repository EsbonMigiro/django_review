from django.urls import path
from . views import movie
from .views import template_view
from .views import details

from myapp import views

urlpatterns=[
    path('movie', movie),
    path('temp', template_view),
    path('details/<int:id>', details),
    path('add', views.add_view), 
    path('details/delete/<int:id>', views.delete)
]