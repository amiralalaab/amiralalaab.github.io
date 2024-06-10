from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def setup_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, age, email, phone, city):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, age, email, phone, city)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, email, phone, city))
    conn.commit()
    conn.close()

def get_all_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return users

def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    users = get_all_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    phone = request.form['phone']
    city = request.form['city']
    if name and age and email and phone and city:
        add_user(name, age, email, phone, city)
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>')
def delete(user_id):
    delete_user(user_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    setup_db()
    app.run(debug=True)
