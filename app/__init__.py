from flask import Flask
from config import Config

app = Flask(__name__)
app._static_folder = './static'

from app import routes
