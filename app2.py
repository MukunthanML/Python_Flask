from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items =[]
class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name']==name:
                return item, 200
        return {'Message': 'Not Found'},404
    def post(self, name):
        item ={"name": name}
        items.append(item)
        return item, 201
class Items(Resource):
   def get(self):
       return {'Items':items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run()

