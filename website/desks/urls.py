from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/floors/<int:site_id>", views.get_floors, name = "get_floors"),
    path("api/desks/<int:floor_id>", views.get_desks, name = "get_desks"),
    path(
        "api/bookings/<int:desk_id>/<str:start_datetime>/<str:end_datetime>", 
        views.get_bookings, 
        name = "get_bookings",
    ),
]