from django.db import models
from django.conf import settings

# Create your models here.

class Room(models.Model):
    ROOM_CATEGORIES=(
        ('EXE', 'EXECUTIVE'),
        ('DEL', 'DELUXE'),
        ('PRE', 'PREMIUM'),
        ('STD', 'STANDARD'),
        ('PNT', 'PENTHOUSE')
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.number} - {self.category}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.user} has booked {self.room} from {self.check_in} to {self.check_out}"

    def get_room_category(self):
        room_categories = dict(self.room.ROOM_CATEGORIES)
        room_category = room_categories.get(self.room.category)
        return room_category

    def get_cancel_booking_url(self):
