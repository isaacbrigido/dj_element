from django.urls import path

from . import views

app_name = 'platforms'

urlpatterns = [
    path('<str:slug>/', views.show_platform, name='show'),
]
