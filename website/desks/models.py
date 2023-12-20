from datetime import datetime, timezone

from django.contrib.auth import get_user_model
from django.db import models

from locations.models import Floor

class Desk(models.Model):
    floor = models.ForeignKey(
        to = 'locations.Floor',
        on_delete = models.CASCADE,
    )
    name = models.CharField(max_length = 254, unique = True)
    height_adjustable = models.BooleanField(default = False)
    
    class Meta:
        db_table = 'desks_desks'


class Booking(models.Model):

    user = models.ForeignKey(
        to = get_user_model(),
        on_delete = models.CASCADE,
    )
    desk = models.ForeignKey(
        to = Desk,
        on_delete = models.CASCADE,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    check_in_requested = models.BooleanField(default = False)
    check_in_received = models.BooleanField(default = False)
    
    def is_concluded(self):
        return self.end_time <= datetime.now(timezone.utc)
    
    class Meta:
        db_table = 'desks_bookings'
    