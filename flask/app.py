from flask import Flask
from flask_cors import *
from api import create_app
import os

app = Flask(__name__)
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    CORS(app)
    app.run()
