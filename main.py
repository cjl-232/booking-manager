import mysql.connector

db = mysql.connector.connect(
    host="DESKTOP-1GE1OCN",
    user="testuser",
    password="testpassword",
    database = 'bookings'
)

print(db)

#Focus on pulling from an example SQL server and uploading to it
#Should have a users table, a bookables table, and a bookings table
#Important to work out how best to handle adding bookables and their references

# import smtplib
# content="Hello World"
# mail=smtplib.SMTP('smtp.gmail.com', 587)
# mail.ehlo()
# mail.starttls()
# sender='conda0924@gmail.com'
# recipient='chrislinnell232@gmail.com'
# mail.login('conda0924@gmail.com','wbwchhedsczhihty')
# header='To:'+recipient+'\n'+'From:' \
# +sender+'\n'+'subject:testmail\n'
# content=header+content
# mail.sendmail(sender, recipient, content)
# mail.close()