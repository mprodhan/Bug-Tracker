from django.urls import path
from ticket import views

urlpatterns = [
    path('', views.index, name='homepage')
]