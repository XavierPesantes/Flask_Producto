import os
from flask import Flask
from flask_restful import reqparse, Api
from classes import Productos, Producto

app = Flask(__name__)

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('producto', type=int, required=True)

api.add_resource(Producto, '/producto/<producto_id>')
api.add_resource(Productos, '/productos')
