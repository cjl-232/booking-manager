#Incorporate SQLAlchemy...

import datetime

import mysql.connector
import pandas as pd

from classes.booking import Booking
from classes.user import User

def _query(
    connection : mysql.connector.Connect,
    base_query : str,
    values : tuple = tuple()
) -> list:

    with self.connection.cursor() as cursor:
        cursor.execute(base_query, values)
        return cursor.fetchall()
    
def addBooking(
    connection : mysql.connector.Connect,
    user_id : int,
    bookable_id : int,
    start : datetime.datetime,
    duration : datetime.timedelta,
) -> bool:

    base_query = 'INSERT INTO bookings (email, hash_value) VALUES (%s, %s);'


def loadUser(
    connection : mysql.connector.Connect,
    user_id : int,
) -> classes.user.User:
    
    