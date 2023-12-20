import datetime
from itertools import repeat

class Booking:
    
    def __init__(
        self,
        start : datetime.datetime,
        duration : datetime.timedelta,
    ):
        self.start = start
        self.duration = duration
        
    def contains(self, datetime: datetime.datetime) -> bool:
        return self.start <= datetime < self.start + self.duration
        
    def intersects(self, booking: 'Booking') -> bool:
        bounds = [booking.start, booking.start + booking.duration]
        return self.contains(bounds[0]) or self.contains(bounds[1])
    
    def isActive(self) -> bool:
        return self.contains(datetime.now())
    
    def isExpired(self) -> bool:
        return self.start + self.duration < datetime.now()
        


class Bookable:

    def __init__(self, bookings : dict = {}):
        self.bookings = bookings
    
    def isAvailable(self, desired_booking : Booking) -> bool:    
        iterables = [
            self.bookings.values(),
            repeat(desired_booking, len(self.bookings))
        ]
        return not any(map(Booking.intersects, *iterables))
        
        
        
    
bookings = { 1: Booking(datetime.datetime(2023, 12, 9), datetime.timedelta(days = 3)), 2: Booking(datetime.datetime(2023, 12, 9), datetime.timedelta(days = 3)), 3: Booking(datetime.datetime(2023, 11, 9), datetime.timedelta(days = 3)) }

clashing_booking = Booking(datetime.datetime(2023, 12, 11), datetime.timedelta(days = 2))

non_clashing_booking = Booking(datetime.datetime(2023, 11, 11), datetime.timedelta(days = 2))

bookable = Bookable(bookings)

print(bookable.isAvailable(clashing_booking))

print(bookable.isAvailable(non_clashing_booking))

class Desk:
    pass
    