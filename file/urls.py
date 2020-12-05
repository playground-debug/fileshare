from django.urls import path
from . import views

urlpatterns = [
    path('uploadfile', views.uploadfile, name='uploadfile'),
    path('portal', views.portal, name='portal'),
]
