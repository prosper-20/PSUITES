from typing import List
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View

from hotel.forms import AvailabilityForm 
from .models import Room, Booking
from hotel.booking_functions.availability import check_availability
# Create your views here.

class RoomListView(ListView):
    model = Room


class BookingList(ListView):
    model = Booking


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
            room_category = self.kwargs.get('category', None)
            room_list = Room.objects.filter(category=category)
            room = room_category[0]
            return render()

        

    def post(self, request, *args, **kwargs):
         room_list = Room.objects.filter(category=category)
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse("This category of rooms are fully booked!")



class BookingView(FormView):
    form_class = AvailabilityForm
    template_name="hotel/availability_form.html"

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse("This category of rooms are fully booked!")
