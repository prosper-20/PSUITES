from django.urls import path
from .views import RoomList, BookingList

app_name = "hotel"

urlpatterns = [
    path("room_list/", RoomList.as_view(), name='RoomList'),
    path("booking-list/", BookingList.as_view(), name="Booking-List"),
]