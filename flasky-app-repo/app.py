# app.py
from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Define a simple route
@app.route('/')
def hello_world():
    return '<h1>Hello from Flasky on Render!</h1>'

# This block is for local development only, Render will use Gunicorn
if __name__ == '__main__':
    app.run(debug=True)
