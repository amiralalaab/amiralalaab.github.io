from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

users = [
    {'id': 1, 'name': 'John Doe', 'age': 30, 'email': 'john@example.com', 'phone': '123456789', 'city': 'New York'},
    {'id': 2, 'name': 'Jane Smith', 'age': 25, 'email': 'jane@example.com', 'phone': '987654321', 'city': 'Los Angeles'}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    new_id = len(users) + 1
    new_user = {
        'id': new_id,
        'name': request.form['name'],
        'age': request.form['age'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'city': request.form['city']
    }
    users.append(new_user)
    return redirect(url_for('index'))

@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    for user in users:
        if user['id'] == user_id:
            user['name'] = request.form['name']
            user['age'] = request.form['age']
            user['email'] = request.form['email']
            user['phone'] = request.form['phone']
            user['city'] = request.form['city']
            break
    return redirect(url_for('index'))

def generate_static_files():
    with app.test_request_context():
        html = render_template('index.html', users=users)
        with open('index.html', 'w') as f:
            f.write(html)

if __name__ == '__main__':
    generate_static_files()
    app.run(debug=True)
