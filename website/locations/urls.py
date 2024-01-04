from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="gallery"),
    #path('<int:floor_id>/', views.floor_plan, name="floor_plan"),
]