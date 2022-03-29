from django.db import models

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
