from services import app, BUILD_DIR
from flask import Flask, Response
from werkzeug.datastructures import Headers

def load_index_file():
  index_file_path = '{}/index.html'.format(BUILD_DIR)
  with open(index_file_path, 'r', encoding='utf-8') as f:
    index_file = f.read()
  return index_file

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000
index_file = load_index_file()

@app.route('/', methods=['GET'])
def index():
  return Response(index_file, mimetype='text/html',
                  headers=Headers({'Cache-Control': 'max-age=60'}))

@app.route('/<path:path>')
def static_file(path):
  return app.send_static_file(path)
