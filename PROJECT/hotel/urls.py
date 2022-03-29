from django.urls import path
from .views import RoomList, BookingList, BookingView


urlpatterns = [
    path("room-list/", RoomList.as_view(), name='RoomList'),
    path("booking-list/", BookingList.as_view(), name="Booking-List"),
    path("book/", BookingView.as_view(), name="booking_view" )
]