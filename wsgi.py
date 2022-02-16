import sys
import logging
from config import APP_DIR, ENV_DIR
from main import app as application

activate_this = ENV_DIR + '/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code, dict(__file__=activate_this))

sys.path.append(ENV_DIR)

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, APP_DIR)


