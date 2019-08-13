from flask import Flask, request, jsonify
from libs import ObjectPool


app = Flask(__name__)

pool = ObjectPool.PoolReusable()

@app.route('/')
def ping():
  data = {
    'env': 'local',
  }
  return jsonify(
    success=True,
    data=data
  )

@app.route('/objectPool')
def objectPool():
  used = pool.use();
  data = {
    'object': pool.available(),
  }
  return jsonify(
    success=True,
    data=data
  )
