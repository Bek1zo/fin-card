"""Debuger."""
from app import get_app
from debug_setting import DevConfig

app = get_app(DevConfig)

from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run(port=5000, host='192.168.31.67', use_debugger=True, use_reloader=True, passthrough_errors=True)
