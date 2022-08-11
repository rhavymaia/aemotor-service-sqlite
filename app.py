from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'get'}

    def post(self):
        return {'hello': 'post'}


api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=False)
