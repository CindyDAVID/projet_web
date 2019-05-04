from django.urls import path
from . import views

urlpatterns = [
    path('', views.home), #il faudra changer la val du truc '' quand on joindra tout

]