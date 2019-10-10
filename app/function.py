import gkeepapi
import os
import json
from . import config

def get_gkeep():
	keep = gkeepapi.Keep()
	if os.path.isfile(config.PATH_TO_FILE):
		with open(config.PATH_TO_FILE, 'r') as f:
			keep.login(config.GOOGLE_LOGIN, config.GOOGLE_PASSWORD, state=json.load(f))
	else:
		with open(config.PATH_TO_FILE, 'w') as f:
			keep.login(config.GOOGLE_LOGIN, config.GOOGLE_PASSWORD)
			json.dump(keep.dump(), f)

	return keep
