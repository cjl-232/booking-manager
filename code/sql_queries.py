#SQLAlchemy incorporated for the most important function.
#Look at the current system's HTML for guidance now

#Incorporate SQLAlchemy...

#The important Python operations here are to identify non-covered ranges.
#It's silly to store huge arrays of time periods in SQL. The focus should be on
#manipulating pandas dataframes, I think

import pandas as pd

from datetime import datetime
from sqlalchemy import and_, create_engine, insert, not_, or_, select
from sqlalchemy import MetaData, Table, URL

#from classes.booking import Booking
#from classes.user import User


#Establish a connection:
_url = URL.create(
    drivername = 'mysql',
    username = 'testuser',
    password = 'testpassword',
    host = 'DESKTOP-1GE1OCN',
    port = 3306,
    database = 'booking_manager',
)
_engine = create_engine(_url)

#Retrieve relevant tables:
_metadata = MetaData()
_metadata.reflect(_engine)


#Function to retrieve available desks between two points in time:
def get_desk_options(
    start_time : datetime,
    end_time : datetime,
    limit : None | list[int] = None,
) -> pd.DataFrame:

    #Alias the necessary tables:
    desks = _metadata.tables['desks']
    bookings = _metadata.tables['bookings']
    
    #Construct the query:
    query = select(desks.c['desk_id', 'desk_name'])
    query = query.join(
        target = bookings,
        onclause = and_(
            desks.c.desk_id == bookings.c.desk_id,
            not_(
                or_(
                    bookings.c.start_time < start_time,
                    bookings.c.end_time > end_time,
                )
            )
        ),
        isouter = True,
    )
    if limit != None:
        query = query.where(desks.c.desk_id.in_(limit))
    query = query.where(bookings.c.desk_id == None)
    
    #Execute the query and return a pandas dataframe:
    return pd.read_sql(query, _engine)

def insert_booking(
    user_id : int,
    desk_id : int,
    start_time : datetime,
    end_time : datetime,
) -> bool:

    #Check if the booking is valid:
    is_valid = not get_desk_options(start, end, [desk_id]).empty
    
    #If so, perform the insertion:
    if is_valid:
    
        #Alias the bookings table:
        bookings = _metadata.tables['bookings']
        
        #Construct an insertion statement:
        statement = insert(bookings).values(
            user_id = user_id,
            desk_id = desk_id,
            start_time = start_time,
            end_time = end_time
        )
        
        #Execute and commit the statement:
        with _engine.connect() as connection:
            connection.execute(statement)
            connection.commit()

    #Return True if insertion occured, False otherwise:
    return is_valid
    
print(insert_booking(1, 1, datetime(2020, 10, 10, 12, 5, 0), datetime(2021, 10, 11, 12, 5, 0)))