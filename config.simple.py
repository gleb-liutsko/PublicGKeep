class ConfigFlask:
	DEBUG = False

class ConfigGKeep:
	EMAIL = ''
	TOKEN = '' # Выполните python "get_token.py" для потучения
	TAG_PUBLIC = 'Public'
	PATH_TO_FILE = './tmp/gkeep.bac'

class ConfigSite:
	NAME = 'Public GKeep' # Указывается в <title>
	COPYRIGHT_TEXT = '(c) Gleb Liutsko'
	COPYRIGHT_URL = 'https://liutsko.site/'
