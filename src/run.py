from flask import Flask
from kernel.controllers import *

app = Flask(__name__)
app.register_blueprint(blueprint)
app.secret_key = 'the_secret_key'

if __name__ == "__main__":
	app.debug = True
	app.run('192.168.56.40', port = 80)