import mysql.connector
from argon2 import PasswordHasher

class MySQLConnection:

    password_hasher = PasswordHasher()
    
    def __init__(
        self,
        user,
        password,
    ):
        self.connection = mysql.connector.connect(
            user = user, 
            password = password,
            database = 'bookings'
        )
    
    #Methods:
    def _query(self, base_query : str, values : tuple = tuple()):
        cursor = self.connection.cursor()
        cursor.execute(base_query, values)
        result = cursor.fetchall()
        cursor.close()
        return result
        
    def addUser(self, email : str, password : str):
        base_query = 'INSERT INTO users (email, hash_value) VALUES (%s, %s);'
        values = (email, self.password_hasher.hash(password))
        self._query(base_query, values)
        self.connection.commit()
        
    def getUserID(self, email : str) -> int:
        base_query = 'SELECT id FROM users WHERE email = %s LIMIT 1;'
        query_result = self._query(base_query, (email,))
        if len(query_result) != 0:
            return query_result[0][0]
        else:
            return None
            
    def createUserObject(self, 
        
        
        
        

connection = MySQLConnection(
    user="testuser",
    password="testpassword",
)

try:
    connection.addUser("kirbykins232@gmail.com", "PAIOH!")

except:
    pass

print(connection.getUserID("kirbykins232@gmail.com"))