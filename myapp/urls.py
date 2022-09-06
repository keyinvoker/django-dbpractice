from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert', views.insert, name='insert'),
    path('update/<int:pk>', views.update, name='update'),
    path('search/<int:pk>', views.search, name='search'),
]