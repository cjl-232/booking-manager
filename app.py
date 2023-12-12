from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to the database
conn = sqlite3.connect('booking_system.db')
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # For simplicity, storing passwords in plaintext (don't use this in production)
    cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
    ''', (username, password))
    conn.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
