from services import app
from flask import Flask, render_template, request, redirect, url_for, Response
import json

@app.route('/services/health-check', methods=['GET'])
def health_check():
  body = {
      'msg': 'Hello World',
  }
  return Response(json.dumps(body), mimetype='application/json')
