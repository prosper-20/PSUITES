from django.urls import reverse
from Core.models import Book

def get_room_list():
    room_list = []
    room_categories = dict(room.ROOM_CATEGORIES)
    
    for category in room_categories:
        room_category = room_categories.get(category)
        room_url = reverse('RoomDetailView', kwargs={'category': room_category})
        room_list.append((room_category, room_url))