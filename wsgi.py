import sys, os

dname = os.path.dirname(os.path.abspath(__file__))
os.chdir(dname)

file_activate = 'venv/bin/activate_this.py'
exec(open(file_activate, 'r').read(), {'__file__': file_activate})
sys.path.insert(0, '.')

import logging
logging.basicConfig(stream=sys.stderr, level=logging.INFO)

from app import app as application
