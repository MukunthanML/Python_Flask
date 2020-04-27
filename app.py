from flask import Flask,jsonify,request

app = Flask(__name__)

products = [{'name':'watch'},
             {'name':'pen'},{'name':'clock'},{'name':'speaker'}]

@app.route('/')
def home():
    return '<h1>Welcome to Flask Introduction today !</h1>'

@app.route('/allproducts',methods=['get'])
def getAllProducts():
    return jsonify({"products": products})

@app.route('/products/<string:name>',methods=['GET'])
def getProduct(name):
    for product in products:
        if product['name']==name:
            return jsonify(product)

    return jsonify({'Error':'Product {} not found !'.format(name)})


@app.route('/addproduct',methods=['POST'])
def addProduct():
    req = request.get_json()
    products.append({'name':req['name']})
    return jsonify(products)

@app.route('/removeproduct/<string:name>',methods=['DELETE'])
def removeProduct(name):
    for product in products:
        if product['name'] == name:
            products.remove(product)
            return jsonify({'Message': 'Product {} is removed'.format(name)})

    return jsonify({'Error': 'Product {} not found !'.format(name)})


if __name__=='__main__':
    app.run()