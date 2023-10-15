#!usr/bin/python3
import sys
import logging


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/don/")

from don  import app as application


application.secret_key = "ikdkekosodkxk4382idjjx"
