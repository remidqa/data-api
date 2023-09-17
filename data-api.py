from flask import Flask
from flask_restx import Resource, Api
from routes.crud import api as ns_cruds


app = Flask(__name__)
api = Api(app)

api.add_namespace(ns_cruds, path='/')



if __name__ == '__main__':
    app.run(debug=True)