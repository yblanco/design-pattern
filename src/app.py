from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def ping():
  data = {
    'env': 'local'
  }
  return jsonify(
    success=True,
    data=data
  )
