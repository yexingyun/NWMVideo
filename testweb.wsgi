import sys

#app's path

sys.path.insert(0,'C:\projecj\NWMVideo')

from main import app
#initialize WSGI app object
application = app

