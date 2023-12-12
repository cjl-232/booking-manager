import numpy as np
from numpy.typing import NDArray

RefIds = np.dtype([('bookable_id', np.int32), ('booking_id', np.int32)])

class User:

    def __init__(
        self,
        email : string,
        bookings : NDArray[RefIds] = np.array([], dtype = RefIds),
    ):
        self.email = email
        self.bookings = bookings