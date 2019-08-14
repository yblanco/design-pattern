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
  reusable = pool.acquire();
  print("After external acquire", pool.available())
  data = {
    'available': pool.use(),
  }
  pool.release(reusable)
  print("After external release", pool.available())
  return jsonify(
    success=True,
    data=data
  )
