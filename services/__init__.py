from flask import Flask

app = Flask(__name__, static_folder='../build', template_folder='../build')
import services.static
import services.views

def run_app():
    return app