#!usr/bin/python
import sys
import logging


from main import app
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/don/")

app.secret_key = "tkcofkkforodo"


if __name__ == "__main__":
    app.run()
