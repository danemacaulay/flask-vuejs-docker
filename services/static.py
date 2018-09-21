from services import app
from flask import Flask, render_template

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/<path:path>')
def static_file(path):
  return app.send_static_file(path)
