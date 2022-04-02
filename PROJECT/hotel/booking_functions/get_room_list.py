from django.urls import reverse
from hotel.models import Room

def get_room_list():
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)

    room_cat_url__list = []
    
    for category in room_categories:
        room_category = room_categories.get(category)
        room_url = reverse('RoomDetailView', kwargs={'category': room_category})
        room_cat_url__list.append((room_category, room_url))

    
    return room_cat_url__list