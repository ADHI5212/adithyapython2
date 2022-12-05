from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='demo'),
    #path('basic/',views.result,name='result'),

]
