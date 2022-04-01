from django.urls import path
from .views import RoomListView, BookingList, RoomDetailView
from django.conf.urls import static
from django.conf import settings


urlpatterns = [
    path("room-list/", RoomListView, name='RoomListView'),
    path("booking-list/", BookingList.as_view(), name="Booking-List"),
    # path("book/", BookingView.as_view(), name="booking_view" ),
    path("room/<category>", RoomDetailView.as_view(), name='RoomDetailView')
]