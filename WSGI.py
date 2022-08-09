import sys
path = '/home/ehsanhrz/Tweebot/'
if path not in sys.path:
   sys.path.append(path)

from f_app import app as application
