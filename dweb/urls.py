from django.urls import path

from . import views
from .views import views_index

urlpatterns = [
    path('', views_index.index, name='index'),
]