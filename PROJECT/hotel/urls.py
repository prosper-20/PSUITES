from django.urls import path
from .views import RoomList, BookingList


urlpatterns = [
    path("room-list/", RoomList.as_view(), name='RoomList'),
    path("booking-list/", BookingList.as_view(), name="Booking-List"),
]