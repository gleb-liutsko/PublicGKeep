import os
from flask import Flask
from . import config

if not os.path.isdir('tmp'):
	os.mkdir('tmp')

app = Flask(__name__)
from . import views
