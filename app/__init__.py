from flask import Flask
from . import config
import gkeepapi

keep = gkeepapi.Keep()
keep.login(config.GOOGLE_LOGIN, config.GOOGLE_PASSWORD)

app = Flask(__name__)
from . import views
