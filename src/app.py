from flask import Flask, request, jsonify
from libs import ObjectPool, AbstractFactory


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


@app.route('/abstractFactory')
def abstractFactory():
  products = list();
  for factory in (AbstractFactory.ConcreteFactory1(), AbstractFactory.ConcreteFactory2()):
    product = factory.create_product();
    products.append(product.create());

  return jsonify(
    success=True,
    data = products
  )