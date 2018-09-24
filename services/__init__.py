from flask import Flask

BUILD_DIR = 'build'
build_path = '../{}'.format(BUILD_DIR)

app = Flask(__name__, static_folder=build_path)

import services.static
import services.views

def run_app():
    return app