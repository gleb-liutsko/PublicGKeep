from config import ConfigGKeep
import gkeepapi
import os
import json

def get_gkeep():
	keep = gkeepapi.Keep()
	if os.path.isfile(ConfigGKeep.PATH_TO_FILE):
		with open(ConfigGKeep.PATH_TO_FILE, 'r') as f:
			keep.resume(ConfigGKeep.EMAIL, ConfigGKeep.TOKEN, state=json.load(f))
	else:
		with open(ConfigGKeep.PATH_TO_FILE, 'w') as f:
			keep.resume(ConfigGKeep.EMAIL, ConfigGKeep.TOKEN)
			json.dump(keep.dump(), f)

	return keep
