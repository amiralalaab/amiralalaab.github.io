from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'id': 1, 'name': 'John Doe', 'age': 30, 'email': 'john@example.com', 'phone': '123456789', 'city': 'New York'},
        {'id': 2, 'name': 'Jane Smith', 'age': 25, 'email': 'jane@example.com', 'phone': '987654321', 'city': 'Los Angeles'}
    ]
    return render_template('index.html', users=users)

def generate_static_files():
    if not os.path.exists('static'):
        os.makedirs('static')
    with app.test_request_context():
        html = render_template('index.html', users=[
            {'id': 1, 'name': 'John Doe', 'age': 30, 'email': 'john@example.com', 'phone': '123456789', 'city': 'New York'},
            {'id': 2, 'name': 'Jane Smith', 'age': 25, 'email': 'jane@example.com', 'phone': '987654321', 'city': 'Los Angeles'}
        ])
        with open('static/index.html', 'w') as f:
            f.write(html)

if __name__ == '__main__':
    generate_static_files()
    app.run(debug=True)
