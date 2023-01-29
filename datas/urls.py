from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('upload/', views.arquivo, name='arquivo'),
    path('datas/', views.datas, name='datas')
]