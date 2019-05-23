from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.index),
    path('create/', views.create),
    # path('', views.index_with_params)
]