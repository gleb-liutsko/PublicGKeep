import os
from flask import Flask
from config import ConfigFlask

if not os.path.isdir('tmp'):
	os.mkdir('tmp')

app = Flask(__name__)
app.config.from_object(ConfigFlask)

from . import views
