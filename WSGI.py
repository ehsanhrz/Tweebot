import sys
path = '/home/ehsanhrz/Tweebot/'
if path not in sys.path:
   sys.path.append(path)

from app import app as application
