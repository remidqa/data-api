from flask import Flask
from flask_restx import Resource, Api
from routes.faq import api as ns_faq


app = Flask(__name__)
api = Api(app)

api.add_namespace(ns_faq, path='/faq')



if __name__ == '__main__':
    app.run(debug=True)